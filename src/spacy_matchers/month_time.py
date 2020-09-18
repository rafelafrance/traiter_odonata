"""Month ranges."""

from .shared import DASH
from .consts import GROUP_STEP, REPLACE

MODIFIER = """ early mid late """.split()


def month_time(span):
    """Enrich the match."""
    data = {}
    modifier, month = '', ''
    for token in span:
        if token.lower_ in MODIFIER:
            modifier = token.lower_
        elif token.ent_type_ == 'month':
            month = REPLACE[token.text.capitalize()]
    data['month_time'] = f'{modifier} {month}'.strip()
    return data


MONTH_TIME = {
    GROUP_STEP: [
        {
            'label': 'month_time',
            'on_match': month_time,
            'patterns': [
                [
                    {'LOWER': {'IN': MODIFIER}, 'OP': '?'},
                    {'LOWER': {'IN': DASH}, 'OP': '?'},
                    {'ENT_TYPE': 'month'},
                ],
            ],
        },
    ],
}
