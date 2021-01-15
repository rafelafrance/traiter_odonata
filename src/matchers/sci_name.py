"""Get scientific names."""

from ..pylib.consts import SLASH


def sci_name(ent):
    """Enrich the match."""
    name = [t.lower_ for t in ent if t._.prev_label == 'odonata'][0].capitalize()
    species = [t.lower_ for t in ent if t._.prev_label == 'odonata_species']
    if species:
        name = [name, f'{name.split()[0]} {species[0]}']
    ent._.data = {'sci_name': name, 'group': 'odonata'}


SCI_NAME = [
    {
        'label': 'sci_name',
        'action': sci_name,
        'patterns': [
            [
                {'ENT_TYPE': 'odonata'},
            ],
            [
                {'ENT_TYPE': 'odonata'},
                {'TEXT': {'IN': SLASH}},
                {'ENT_TYPE': 'odonata_species'},
            ],
        ],
    },
]
