"""Get scientific names."""

from ..pylib.util import GROUP_STEP, SLASH


def sci_name(span):
    """Enrich the match."""
    name = [t.lower_ for t in span if t.ent_type_ == 'odonata'][0].capitalize()
    species = [t.lower_ for t in span if t.ent_type_ == 'odonata_species']
    if species:
        name = [name, f'{name.split()[0]} {species[0]}']
    return {'sci_name': name, 'group': 'odonata'}


SCI_NAME = {
    GROUP_STEP: [
        {
            'label': 'sci_name',
            'on_match': sci_name,
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
    ],
}
