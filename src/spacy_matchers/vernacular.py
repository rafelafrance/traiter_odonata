"""Get common names."""

from .consts import REPLACE, TRAIT_STEP


def vernacular(span):
    """Enrich the match."""
    data = {'sci_name': REPLACE[span.lower_], 'group': span[0].ent_type_}
    return data


VERNACULAR = {
    TRAIT_STEP: [
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
