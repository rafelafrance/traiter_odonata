"""Base matcher object."""

from traiter.matcher import TraitMatcher  # pylint: disable=import-error

from .flight_period import FLIGHT_PERIOD
from .header import HEADER
from .month_time import MONTH_TIME
from .range import RANGE
from .scientific_name import SCI_NAME
from .total_length import TOTAL_LENGTH
from .vernacular import VERNACULAR
from ..pylib.terms import TERMS

MATCHERS = (
    FLIGHT_PERIOD, HEADER, MONTH_TIME, RANGE,
    SCI_NAME, TOTAL_LENGTH, VERNACULAR,
)


class Matcher(TraitMatcher):
    """Base matcher object."""

    def __init__(self, nlp):
        super().__init__(nlp)

        terms = TERMS
        self.add_terms(terms)

        groups = []
        traiters = []
        headers = []

        for matcher in MATCHERS:
            groups += matcher.get('groupers', [])
            traiters += matcher.get('traits', [])
            headers += matcher.get('headers', [])

        self.add_patterns(groups, 'groups')
        self.add_patterns(traiters, 'traits')
        self.add_patterns(headers, 'headers')
