"""Get common names."""

from ..pylib.terms import REPLACE


def vernacular(span):
    """Enrich the match."""
    data = {'sci_name': REPLACE[span.lower_], 'group': span[0].ent_type_}
    return data


VERNACULAR = {
    'name': 'vernacular',
    'traits': [
        {
            'label': 'vernacular',
            'on_match': vernacular,
            'patterns': [
                [
                    {'ENT_TYPE': 'common_name'},
                ],
            ],
        },
    ],
}
