"""Sex terms."""

from ..pylib.util import REPLACE, TRAIT_STEP


SIMILAR = """like similar""".split()


def sex(span):
    """Enrich a phrase match."""
    return {'sex': REPLACE.get(span.lower_, span.lower_)}


def not_sex(_):
    """Handle similar to notations for sex."""
    return {'_forget': True}


SEX = {
    TRAIT_STEP: [
        {
            'label': 'sex',
            'on_match': sex,
            'patterns': [
                [
                    {'ENT_TYPE': 'gender'},
                ],
            ],
        },
        {
            'label': 'not_sex',
            'on_match': not_sex,
            'patterns': [
                [
                    {'LOWER': {'IN': SIMILAR}},
                    {'POS': {'IN': ['ADP']}, 'OP': '?'},
                    {'ENT_TYPE': 'gender'},
                ],
            ],
        },
    ],
}
