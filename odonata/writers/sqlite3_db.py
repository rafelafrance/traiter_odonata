"""Write data to a duck_db."""

import logging
import os
import sqlite3
from datetime import datetime

import pandas as pd


def sqlite3_db(args, rows):
    """Write data to a duck_db."""
    logging.info('Writing to database.')

    if args.clear_db:
        args.db.unlink(missing_ok=True)

    cxn = sqlite3.connect(str(args.db))

    create_tables(cxn)
    delete_old_recs(args, cxn)

    source_df = get_sources(args, rows, cxn)
    trait_df, field_df = get_traits(rows, cxn)

    source_df.to_sql('sources', cxn, if_exists='append', index=False)
    trait_df.to_sql('traits', cxn, if_exists='append', index=False)
    field_df.to_sql('fields', cxn, if_exists='append', index=False)

    cxn.close()


def delete_old_recs(args, cxn):
    """Remove old records before inserting new ones."""
    sql = f'select source_id from sources where guide = ? limit 1'
    try:
        source_id = cxn.execute(sql, (args.text_file.name,)).fetchone()[0]
        for table in ('sources', 'traits', 'fields'):
            sql = f"""delete from {table} where source_id = ?;"""
            cxn.execute(sql, (source_id,))
            cxn.commit()
    except (TypeError, sqlite3.OperationalError):
        pass


def get_traits(rows, cxn):
    """Build traits data frame."""
    trait_df = []
    field_df = []

    trait_id = get_max_id(cxn, 'traits')

    for row in rows:
        for trait in row['traits']:
            trait_id += 1
            trait_rec = {
                'trait_id': trait_id,
                'source_id': row['source_id'],
                'trait': trait['trait'],
                'taxon': row['taxon'],
                'part': trait.get('body_part', ''),
                'sex': trait.get('sex', ''),
            }
            trait_df.append(trait_rec)

            for field, value in trait.items():
                if field in ('trait',):
                    continue
                field_rec = {
                    'source_id': row['source_id'],
                    'trait_id': trait_id,
                    'field': field,
                    'value': value,
                }
                field_df.append(field_rec)

    trait_df = pd.DataFrame(trait_df)
    field_df = pd.DataFrame(field_df)

    return trait_df, field_df


def get_max_id(cxn, table):
    """Get the max ID from a table in the database."""
    column = table[:-1] + '_id'
    sql = f'SELECT MAX({column}) FROM {table};'
    try:
        return cxn.execute(sql).fetchone()[0] or 0
    except sqlite3.OperationalError:
        return 0


def get_sources(args, rows, cxn):
    """Build sources data frame."""
    df = []

    converted = os.stat(args.text_file).st_mtime
    converted = datetime.fromtimestamp(converted)
    converted = converted.isoformat(sep=' ', timespec='seconds')

    extracted = datetime.now().isoformat(sep=' ', timespec='seconds')

    source_id = get_max_id(cxn, 'sources')

    for row in rows:
        source_id += 1
        source = {
            'source_id': source_id,
            'guide': row['guide'],
            'text_': row['text'],
            'converted': converted,
            'extracted': extracted,
        }
        df.append(source)
        row['source_id'] = source_id

    df = pd.DataFrame(df)
    return df


def create_tables(cxn):
    """Create tables and indices."""
    cxn.executescript("""
        CREATE TABLE IF NOT EXISTS sources (
            source_id INTEGER PRIMARY KEY,
            guide     TEXT,
            text_     TEXT,
            converted DATE,
            extracted DATE
        );
        CREATE INDEX IF NOT EXISTS sources_source ON sources (guide);
    """)

    cxn.executescript("""
        CREATE TABLE IF NOT EXISTS traits (
            trait_id  INTEGER PRIMARY KEY,
            source_id INTEGER,
            trait     TEXT,
            taxon     TEXT,
            part      TEXT,
            sex       TEXT
        );
        CREATE INDEX IF NOT EXISTS traits_source_id ON traits (source_id);
        CREATE INDEX IF NOT EXISTS traits_trait ON traits (trait);
        CREATE INDEX IF NOT EXISTS traits_taxon ON traits (taxon);
        CREATE INDEX IF NOT EXISTS traits_part ON traits (part);
        CREATE INDEX IF NOT EXISTS traits_sex ON traits (sex);
    """)

    cxn.executescript("""
        CREATE TABLE IF NOT EXISTS fields (
            trait_id  INTEGER,
            source_id INTEGER,
            field     TEXT,
            value
        );
        CREATE INDEX IF NOT EXISTS fields_source_id ON fields (source_id);
        CREATE INDEX IF NOT EXISTS fields_trait_id ON fields (trait_id);
        CREATE INDEX IF NOT EXISTS fields_field ON fields (field);
    """)
