"""Sex terms."""

from ..pylib.actions import text_action
from ..pylib.consts import GROUP_STEP

SIMILAR = """like similar""".split()

SEX = {
    GROUP_STEP: [
        {
            'label': 'sex_diff',
            'on_match': text_action,
            'patterns': [
                [
                    {'LOWER': {'IN': SIMILAR}},
                    {'POS': {'IN': ['ADP']}, 'OP': '?'},
                    {'ENT_TYPE': 'sex'},
                    {'POS': {'IN': ['CCONJ']}, 'OP': '?'},
                ],
            ],
        },
    ],
}
