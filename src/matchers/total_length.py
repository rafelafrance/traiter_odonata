"""Get total length measurements."""

from ..pylib.terms import REPLACE


def total_length(span):
    """Enrich the match."""
    data = {}
    for token in span:
        if token.ent_type_ == 'range':
            data['low'] = token._.data['low']
            data['high'] = token._.data['high']
        elif token.ent_type_ == 'length_units':
            data['units'] = REPLACE[token.lower_]
    return data


TOTAL_LENGTH = {
    'name': 'total_length',
    'traits': [
        {
            'label': 'total_length',
            'on_match': total_length,
            'patterns': [
                [
                    {'ENT_TYPE': 'total_length'},
                    {'ENT_TYPE': 'range'},
                    {'ENT_TYPE': 'length_units'},
                ],
            ],
        },
    ],
}
