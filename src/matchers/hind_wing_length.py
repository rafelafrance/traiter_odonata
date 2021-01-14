"""Get total the hind wing length."""

from functools import partial

from traiter.actions import hoist_action

HIND_WING_LENGTH = [
    {
        'label': 'hind_wing_length',
        'action': partial(hoist_action, keys={'low', 'high'}),
        'patterns': [
            [
                {'ENT_TYPE': 'hind_wing_length_key'},
                {'ENT_TYPE': 'range'},
            ],
        ],
    },
]
