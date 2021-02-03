"""Get scientific names."""

import spacy

from odonata.pylib.token import COMPILE_MATCHES

SCI_NAME = [
    {
        'label': 'sci_name',
        'on_match': 'sci_name.v1',
        'patterns': COMPILE_MATCHES(
            None,
            'odonata',
            'odonata / odonata_species',
        )
    },
]


@spacy.registry.misc(SCI_NAME[0]['on_match'])
def sci_name(ent):
    """Enrich the match."""
    name = [t.lower_ for t in ent if t._.cached_label == 'odonata'][0].capitalize()
    species = [t.lower_ for t in ent if t._.cached_label == 'odonata_species']
    if species:
        name = [name, f'{name.split()[0]} {species[0]}']
    ent._.data = {'sci_name': name, 'group': 'odonata'}
