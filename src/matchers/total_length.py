"""Get total the total length."""

from .range import RANGE_ACTION

TOTAL_LENGTH = [
    {
        'label': 'total_length',
        'action': RANGE_ACTION,
        'patterns': [
            [
                {'ENT_TYPE': 'total_length_key'},
                {'ENT_TYPE': 'range'},
            ],
        ],
    },
]
