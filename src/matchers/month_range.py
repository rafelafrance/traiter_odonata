"""Month ranges."""

from ..pylib.consts import DASH, REPLACE

MODIFIER = """ early mid late """.split()
TO = """ to into """.split()


def month_range(span):
    """Enrich the match."""
    modifier = ''
    months = []
    for token in span:
        if token.lower_ in MODIFIER:
            modifier = token.lower_
        elif token.ent_type_ == 'month':
            month = REPLACE[token.text.capitalize()]
            month = f'{modifier} {month}'.strip() if modifier else month
            months.append(month)
            modifier = ''

    data = {f: v for f, v in zip(['from', 'to'], months)}
    return data


MONTH_RANGE = [
    {
        'label': 'month_range',
        'action': month_range,
        'patterns': [
            [
                {'LOWER': {'IN': MODIFIER}, 'OP': '?'},
                {'LOWER': {'IN': DASH}, 'OP': '?'},
                {'ENT_TYPE': 'month'},
            ],
            [
                {'LOWER': {'IN': MODIFIER}, 'OP': '?'},
                {'LOWER': {'IN': DASH}, 'OP': '?'},
                {'ENT_TYPE': 'month'},
                {'LOWER': {'IN': TO}},
                {'LOWER': {'IN': MODIFIER}, 'OP': '?'},
                {'LOWER': {'IN': DASH}, 'OP': '?'},
                {'ENT_TYPE': 'month'},
            ],
        ],
    },
]
