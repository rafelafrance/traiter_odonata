"""Get scientific names."""

from ..pylib.terms import REPLACE


def sci_name(span):
    """Enrich the match."""
    return {'sci_name': REPLACE[span.lower_], 'group': span[0].ent_type_}


SCI_NAME = {
    'name': 'sci_name',
    'traits': [
        {
            'label': 'sci_name',
            'on_match': sci_name,
            'patterns': [
                [
                    {'ENT_TYPE': 'odonata'},
                ],
            ],
        },
    ],
}
