"""Constants used in multiple modules."""

from pathlib import Path

from traiter.terms.itis import Itis

VOCAB_DIR = Path.cwd() / 'src' / 'vocabulary'

TERMS = Itis.shared('animals insect_anatomy units colors')
TERMS += Itis.read_csv(VOCAB_DIR / 'odonata_terms.csv')
TERMS += Itis.read_csv(VOCAB_DIR / 'odonata_species.csv')
TERMS += Itis.itis_common_names(taxon='Odonata')
TERMS += Itis.abbrev_species(TERMS, label='odonata')
TERMS += Itis.taxon_level_terms(
    TERMS, label='odonata', new_label='odonata_species')
TERMS.drop('imperial_length')

REPLACE = TERMS.pattern_dict('replace')

MISSING = """ without missing lack lacking except excepting not """.split()
