"""Sex terms."""

from ..pylib.util import REPLACE, TRAIT_STEP


SIMILAR = """like similar""".split()


def sex(span):
    """Enrich a phrase match."""
    return {'sex': REPLACE.get(span.lower_, span.lower_)}


def sex_comparison(span):
    """Handle similar to notations for sex."""
    return {'sex_comparison': REPLACE.get(span.lower_, span.lower_)}


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
            'label': 'sex_comparison',
            'on_match': sex_comparison,
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
