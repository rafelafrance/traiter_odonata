"""Get scientific names."""

from functools import partial

from ..pylib.actions import flag_action
from ..pylib.consts import HEADER_STEP, INT


HEADER = {
    HEADER_STEP: [
        {
            'label': 'header',
            'on_match': partial(flag_action, flag='in_header'),
            'patterns': [
                [
                    {'TEXT': {'REGEX': INT}},
                    {'ENT_TYPE': 'vernacular'},
                    {'ENT_TYPE': 'sci_name'},
                    {'ENT_TYPE': 'total_length'},
                    {'IS_PUNCT': True, 'OP': '?'},
                    {'ENT_TYPE': 'hind_wing_length'},
                ],
            ],
        },
    ],
}
