"""Get scientific names."""

from spacy import registry
from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.pylib.const import COMMON_PATTERNS

SCI_NAME = MatcherPatterns(
    'sci_name', on_match='sci_name.v1', decoder=COMMON_PATTERNS,
    patterns=[
        'odonata',
        'odonata / odonata_species',
    ],
)


@registry.misc(SCI_NAME.on_match)
def sci_name(ent):
    """Enrich the match."""
    name = [t.lower_ for t in ent if t._.cached_label == 'odonata'][0].capitalize()
    species = [t.lower_ for t in ent if t._.cached_label == 'odonata_species']
    if species:
        name = [name, f'{name.split()[0]} {species[0]}']
    ent._.data = {'sci_name': name, 'group': 'odonata'}
