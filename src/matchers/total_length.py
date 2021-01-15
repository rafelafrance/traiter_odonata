"""Get total the total length."""

from .range import range_

TOTAL_LENGTH = [
    {
        'label': 'total_length',
        'action': range_,
        'patterns': [
            [
                {'ENT_TYPE': 'total_length_key'},
                {'ENT_TYPE': 'range'},
            ],
        ],
    },
]
