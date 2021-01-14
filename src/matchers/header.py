"""Get document headers."""


HEADER = [
    {
        'label': 'header',
        'patterns': [
            [{'TEXT': 'Description'}],
            [{'TEXT': 'Flight'}, {'TEXT': 'Season'}],
            [{'TEXT': 'Identification'}],
            [{'TEXT': 'Natural'}, {'TEXT': 'History'}],
        ],
    },
]
