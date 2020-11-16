"""Get common names."""

from ..pylib.util import REPLACE, TRAIT_STEP


def vernacular(span):
    """Enrich the match."""
    data = {
        'sci_name': REPLACE.get(span.lower_, span.lower_.capitalize()),
        'vernacular': span.lower_}
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
