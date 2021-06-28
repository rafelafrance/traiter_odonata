"""Habitat patterns."""

from spacy import registry
from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.pylib.const import CATEGORY, REPLACE

HABITAT = MatcherPatterns(
    'habitat',
    on_match='odonata.habitat.v1',
    decoder={
        'habitat': {'ENT_TYPE': 'habitat'},
    },
    patterns=[
        'habitat',
    ],
)


@registry.misc(HABITAT.on_match)
def habitat(ent):
    """Enrich the match."""
    data = {}
    lower = ent.text.lower()

    data['habitat'] = REPLACE.get(lower, lower)
    data['habitat_cat'] = CATEGORY.get(lower, lower)

    ent._.data = data
