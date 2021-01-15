"""Get total the hind wing length."""

from .range import range_

HIND_WING_LENGTH = [
    {
        'label': 'hind_wing_length',
        'action': range_,
        'patterns': [
            [
                {'ENT_TYPE': 'hind_wing_length_key'},
                {'ENT_TYPE': 'range'},
            ],
        ],
    },
]
