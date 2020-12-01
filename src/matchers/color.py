"""Common color snippets."""

from ..pylib.actions import text_action
from ..pylib.util import DASH, GROUP_STEP, MISSING

COLORS = ['color', 'color_modifier']
JOINERS = DASH + ['with']


def color(span):
    """Enrich the match."""
    data = text_action(span)
    if [t for t in span if t.lower_ in MISSING]:
        data['missing'] = True
    return data


COLOR = {
    GROUP_STEP: [
        {
            'label': 'color',
            'on_match': color,
            'patterns': [
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '*'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '*'},
                ],
            ],
        },
    ],
}
