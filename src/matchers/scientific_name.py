"""Get scientific names."""

from ..pylib.util import REPLACE, TRAIT_STEP


def sci_name(span):
    """Enrich the match."""
    return {
        'sci_name': REPLACE.get(span.lower_, span.lower_.capitalize()),
        'group': span[0].ent_type_,
    }


SCI_NAME = {
    TRAIT_STEP: [
        {
            'label': 'sci_name',
            'on_match': sci_name,
            'patterns': [
                [
                    {'ENT_TYPE': 'odonata'},
                ],
            ],
        },
    ],
}
