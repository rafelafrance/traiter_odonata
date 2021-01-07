"""Get total the hind wing length."""

from functools import partial

from ..pylib.actions import hoist_action
from ..pylib.consts import TRAIT_STEP

HIND_WING_LENGTH = {
    TRAIT_STEP: [
        {
            'label': 'hind_wing_length',
            'on_match': partial(hoist_action, keys={'low', 'high'}),
            'patterns': [
                [
                    {'ENT_TYPE': 'hind_wing_length_key'},
                    {'ENT_TYPE': 'range'},
                ],
            ],
        },
    ],
}
