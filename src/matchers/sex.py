"""Sex terms."""

from ..pylib.util import GROUP_STEP

SIMILAR = """like similar""".split()

SEX = {
    GROUP_STEP: [
        {
            'label': 'sex_comparison',
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
