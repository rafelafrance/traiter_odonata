"""Get hind wing length measurements."""

from ..pylib.util import REPLACE, TRAIT_STEP


def hind_wing_length(span):
    """Enrich the match."""
    data = {}
    for token in span:
        if token.ent_type_ == 'range':
            data['low'] = token._.data['low']
            data['high'] = token._.data['high']
        elif token.ent_type_ == 'length_units':
            data['units'] = REPLACE[token.lower_]

    data['units'] = data.get('units', 'mm')

    return data


HIND_WING_LENGTH = {
    TRAIT_STEP: [
        {
            'label': 'hind_wing_length',
            'on_match': hind_wing_length,
            'patterns': [
                [
                    {'ENT_TYPE': 'hind_wing_length_key'},
                    {'ENT_TYPE': 'range'},
                    {'ENT_TYPE': 'length_units', 'OP': '?'},
                ],
            ],
        },
    ],
}
