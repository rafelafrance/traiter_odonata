"""Get total the total length."""

from functools import partial

from traiter.actions import hoist_action

TOTAL_LENGTH = [
    {
        'label': 'total_length',
        'action': partial(hoist_action, keys={'low', 'high'}),
        'patterns': [
            [
                {'ENT_TYPE': 'total_length_key'},
                {'ENT_TYPE': 'range'},
            ],
        ],
    },
]
