"""Get terms from various sources (CSV files or SQLite database."""

import csv
import sqlite3

from .util import DATA_DIR, VOCAB_DIR

ODONATA_TERMS = VOCAB_DIR / 'odonata.csv'
COMMON_TERMS = VOCAB_DIR / 'common.csv'
ITIS_DB = DATA_DIR / 'ITIS.sqlite'


def read_terms(term_path):
    """Read and cache the terms."""
    with open(term_path) as term_file:
        reader = csv.DictReader(term_file)
        return list(reader)


TERMS = read_terms(ODONATA_TERMS)
TERMS += read_terms(COMMON_TERMS)

REPLACE = {t['pattern']: r for t in TERMS if (r := t.get('replace'))}


def itis_terms(name, kingdom_id=5, rank_id=220, abbrev=False, species=False):
    """Get terms from the ITIS database.

        kingdom_id =   5 == Animalia
        rank_id    = 220 == Species
    """
    # TODO Bypass using this in tests for now.
    if not ITIS_DB.exists():
        print('Could not find ITIS database.')
        return []

    select_tsn = """ select tsn from taxonomic_units where unit_name1 = ?; """
    select_names = """
        select complete_name
          from hierarchy
          join taxonomic_units using (tsn)
         where hierarchy_string like ?
           and kingdom_id = ?
           and rank_id = ?;
           """

    with sqlite3.connect(ITIS_DB) as cxn:
        cursor = cxn.execute(select_tsn, (name,))
        tsn = cursor.fetchone()[0]
        mask = f'%-{tsn}-%'
        taxa = {n[0].lower() for n in
                cxn.execute(select_names, (mask, kingdom_id, rank_id))}

    terms = []
    name = name.lower()
    for taxon in sorted(taxa):
        terms.append({
            'label': name,
            'pattern': taxon,
            'attr': 'lower',
            'replace': taxon.capitalize(),
        })
        if abbrev:
            words = taxon.split()
            if len(words) > 1:
                first, *rest = words
                first = first[0]
                rest = ' '.join(rest)
                terms.append({
                    'label': name,
                    'pattern': f'{first}. {rest}',
                    'attr': 'lower',
                    'replace': taxon.capitalize(),
                })
        if species:
            words = taxon.split()
            if len(words) > 1:
                genus, species, *rest = words
                terms.append({
                    'label': 'species',
                    'pattern': species,
                    'attr': 'lower',
                    'replace': species.lower(),
                })

    for term in terms:
        REPLACE[term['pattern']] = term['replace']

    return terms


def get_common_names(name, kingdom_id=5, rank_id=220):
    """Guides often use common names instead of scientific name.

        kingdom_id =   5 == Animalia
        rank_id    = 220 == Species
    """
    # TODO Bypass using this in tests for now.
    if not ITIS_DB.exists():
        print('Could not find ITIS database.')
        terms = [
            {
                'label': 'common_name',
                'pattern': 'western red damsel',
                'attr': 'lower',
                'replace': 'Amphiagrion saucium',
            },
            {
                'label': 'common_name',
                'pattern': 'plains clubtail',
                'attr': 'lower',
                'replace': 'Gomphurus externus',
            },
        ]
        for term in terms:
            REPLACE[term['pattern']] = term['replace']
        return terms

    select_tsn = """ select tsn from taxonomic_units where unit_name1 = ?; """
    select_names = """
    select vernacular_name, complete_name
      from vernaculars
      join taxonomic_units using (tsn)
      join hierarchy using (tsn)
     where hierarchy_string like ?
       and kingdom_id = ?
       and rank_id = ?;
        """

    with sqlite3.connect(ITIS_DB) as cxn:
        cursor = cxn.execute(select_tsn, (name,))
        tsn = cursor.fetchone()[0]
        mask = f'%-{tsn}-%'
        names = {n[0].lower(): n[1] for n in
                 cxn.execute(select_names, (mask, kingdom_id, rank_id))}

    terms = []
    for common, sci_name in names.items():
        terms.append({
            'label': 'common_name',
            'pattern': common,
            'attr': 'lower',
            'replace': sci_name,
        })

    for term in terms:
        REPLACE[term['pattern']] = term['replace']

    return terms
