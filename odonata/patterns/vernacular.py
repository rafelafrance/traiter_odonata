"""Get common names."""

import re

from spacy import registry
from traiter.const import SLASH
from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.pylib.const import COMMON_PATTERNS

SLASH_RE = re.compile('|'.join(SLASH))

VERNACULAR = MatcherPatterns(
    'vernacular', on_match='vernacular.v1', decoder=COMMON_PATTERNS,
    patterns=[
        'common_name',
        'a-z+ / common_name',
    ],
)


@registry.misc(VERNACULAR.on_match)
def vernacular(ent):
    """Enrich the match."""
    name = [t.lower_ for t in ent if t._.cached_label == 'common_name'][0]
    first = SLASH_RE.split(ent.text)
    if len(first) > 1:
        name = [name, f'{first[0]} {" ".join(name.split()[1:])}']
    ent._.data = {'vernacular': name}
