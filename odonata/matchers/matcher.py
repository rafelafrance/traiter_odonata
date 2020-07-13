"""Base matcher object."""

from traiter.trait_matcher import TraitMatcher  # pylint: disable=import-error

from .scientific_name import SCI_NAME
from .vernacular import VERNACULAR
from ..pylib.terms import TERMS, get_common_names, itis_terms

MATCHERS = (
    SCI_NAME, VERNACULAR)


class Matcher(TraitMatcher):
    """Base matcher object."""

    def __init__(self, nlp, attach=True, as_entities=True):
        super().__init__(nlp, as_entities=as_entities)

        terms = TERMS
        terms += itis_terms('Odonata', abbrev=True)
        terms += get_common_names('Odonata')
        self.add_terms(terms)

        traiters = []
        attachers = []

        for matcher in MATCHERS:
            traiters += matcher.get('traits', [])
            attachers += matcher.get('attachers', [])

        self.add_patterns(traiters, 'traits')
        if attach:
            self.add_patterns(attachers, 'attachers')
