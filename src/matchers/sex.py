"""Sex terms."""

from functools import partial

from traiter.actions import text_action

from ..pylib.consts import GROUP_STEP, REPLACE

SIMILAR = """like similar""".split()

SEX = {
    GROUP_STEP: [
        {
            'label': 'sex_diff',
            'on_match': partial(text_action, replace=REPLACE),
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
