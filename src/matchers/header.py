"""Get scientific names."""

from ..pylib.util import CLOSE, COMMA, HEADER_STEP, OPEN


def header(span):
    """Enrich the match."""
    for token in span:
        if token.ent_type_:
            token._.data['in_header'] = True
    return {'_forget': True}


HEADER = {
    HEADER_STEP: [
        {
            'label': 'header',
            'on_match': header,
            'patterns': [
                [
                    {'ENT_TYPE': 'sci_name'},
                    {'IS_SPACE': True, 'OP': '?'},
                    {'TEXT': {'IN': OPEN}},
                    {'ENT_TYPE': 'vernacular'},
                    {'TEXT': {'IN': CLOSE}},
                ],
            ],
        },
        {
            'label': 'header',
            'on_match': header,
            'patterns': [
                [
                    {'IS_DIGIT': True},
                    {'ENT_TYPE': 'vernacular'},
                    {'ENT_TYPE': 'sci_name'},
                    {'ENT_TYPE': 'total_length'},
                    {'TEXT': {'IN': COMMA}, 'OP': '?'},
                    {'ENT_TYPE': 'hind_wing_length'},
                ],
            ],
        },
    ],
}
