"""Get scientific names."""

from ..pylib.terms import REPLACE
from ..pylib.util import TRAIT_STEP


def sci_name(span):
    """Enrich the match."""
    return {'sci_name': REPLACE[span.lower_], 'group': span[0].ent_type_}


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