"""Write data to a duck_db."""

import logging
import os
import sqlite3
from datetime import datetime

from traiter.util import as_list

import pandas as pd


def sqlite3_db(args, rows):
    """Write data to a duck_db."""
    logging.info('Writing to database.')

    if args.clear_db:
        args.db.unlink(missing_ok=True)

    cxn = sqlite3.connect(str(args.db))

    delete_old_recs(args, cxn)

    source_df = get_sources(args, rows, cxn)
    trait_df = get_traits(rows)

    source_df.to_sql('sources', cxn, if_exists='append', index=False)
    trait_df.to_sql('traits', cxn, if_exists='append', index=False)

    cxn.close()


def delete_old_recs(args, cxn):
    """Remove old records before inserting new ones."""
    sql_traits = """
        delete from traits
        where source_id in (select source_id from sources where guide = ?);
        """
    sql_sources = """ delete from sources where guide = ?; """
    try:
        cxn.execute(sql_traits, (args.text_file.name,))
        cxn.execute(sql_sources, (args.text_file.name,))
    except (TypeError, sqlite3.OperationalError) as err:
        logging.info(err)


def get_traits(rows):
    """Build traits data frame."""
    trait_df = []

    for row in rows:
        for trait in row['traits']:
            body_parts = as_list(trait.get('body_part', ''))
            for part in body_parts:
                rec = {
                    'source_id': row['source_id'],
                    'trait': trait['trait'],
                    'taxon': row['taxon'],
                    'body_part': part,
                }

                for field, value in trait.items():
                    if field in ('trait', 'body_part', 'sci_name'):
                        continue
                    rec[field] = value

                trait_df.append(rec)

    trait_df = pd.DataFrame(trait_df)

    return trait_df


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
