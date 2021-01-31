"""Get document headers."""

DOC_HEADING = [
    {
        'label': 'doc_heading',
        'patterns': [
            [{'TEXT': 'Description'}],
            [{'TEXT': 'Flight'}, {'TEXT': 'Season'}],
            [{'TEXT': 'Identification'}],
            [{'TEXT': 'Natural'}, {'TEXT': 'History'}],
        ],
    },
]
