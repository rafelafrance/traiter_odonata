"""Get total the total length."""

from functools import partial

from traiter.actions import hoist_action

from ..pylib.consts import TRAIT_STEP

TOTAL_LENGTH = {
    TRAIT_STEP: [
        {
            'label': 'total_length',
            'on_match': partial(hoist_action, keys={'low', 'high'}),
            'patterns': [
                [
                    {'ENT_TYPE': 'total_length_key'},
                    {'ENT_TYPE': 'range'},
                ],
            ],
        },
    ],
}
