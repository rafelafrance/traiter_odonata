"""Extract body part annotations."""

from ..pylib.actions import text_action
from ..pylib.util import GROUP_STEP

PART = ['part', 'fly']
ANY_PART = PART + ['part_location']

BODY_PART = {
    GROUP_STEP: [
        {
            'label': 'body_part',
            'on_match': text_action,
            'patterns': [
                [
                    {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '*'},
                    {'ENT_TYPE': {'IN': PART}, 'OP': '+'},
                    {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '*'},
                ],
                [
                    {'POS': 'ADJ'},
                    {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
                ],
            ],
        },
    ],
}
