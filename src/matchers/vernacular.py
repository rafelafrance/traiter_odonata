"""Get common names."""

from ..pylib.util import SLASH, TRAIT_STEP


def vernacular(span):
    """Enrich the match."""
    return {'vernacular': span.lower_}


def double_vernacular(span):
    """Handle a double scientific name."""
    common, partial = '', ''
    for token in span:
        if token.ent_type_ == 'common_name':
            common = token.lower_.capitalize()
        elif token.is_alpha:
            partial = token.lower_

    other = f'{partial} {" ".join(common.split()[1:])}'.capitalize()
    data = {'vernacular': [other, common]}
    return data


VERNACULAR = {
    TRAIT_STEP: [
        {
            'label': 'vernacular',
            'on_match': vernacular,
            'patterns': [
                [
                    {'ENT_TYPE': 'common_name'},
                ],
            ],
        },
        {
            'label': 'vernacular',
            'on_match': double_vernacular,
            'patterns': [
                [
                    {'IS_ALPHA': True},
                    {'TEXT': {'IN': SLASH}},
                    {'ENT_TYPE': 'common_name'},
                ],
            ],
        },
    ],
}
