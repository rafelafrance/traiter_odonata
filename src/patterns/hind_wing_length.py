"""Get total the hind wing length."""

from .range import RANGE_ACTION

HIND_WING_LENGTH = [
    {
        'label': 'hind_wing_length',
        'on_match': RANGE_ACTION,
        'patterns': [
            [
                {'ENT_TYPE': 'hind_wing_length_key'},
                {'ENT_TYPE': 'range'},
            ],
        ],
    },
]
