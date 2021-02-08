"""Sex terms."""

from traiter.actions import text_action
from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.pylib.const import REPLACE


def sex(ent):
    """Enrich the match."""
    text_action(ent, REPLACE)


SEX = MatcherPatterns(
    'sex',
    on_match=sex,
    patterns=[[{'ENT_TYPE': 'sex'}]],
)
