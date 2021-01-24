"""Build the NLP trait_pipeline."""

import spacy
from traiter.pattern_utils import add_ruler_patterns
from traiter.pipes import cache, debug, dependency, sentence
from traiter.pipes.entity_data import EntityData

from src.patterns.body_part import BODY_PART, SEGMENTS
from src.patterns.body_part_linker import BODY_PART_LINKER
from src.patterns.color import COLOR
from src.patterns.doc_heading import DOC_HEADING
from src.patterns.hind_wing_length import HIND_WING_LENGTH
from src.patterns.range import RANGE
from src.patterns.sci_name import SCI_NAME
from src.patterns.sex import SEX
from src.patterns.sex_diff import SEX_DIFF, SEX_DIFF_LINKER
from src.patterns.total_length import TOTAL_LENGTH
from src.patterns.vernacular import VERNACULAR
from src.pylib.consts import TERMS

MATCHERS1 = [DOC_HEADING, RANGE, SEGMENTS]

MATCHERS2 = [
    BODY_PART, COLOR, HIND_WING_LENGTH, SCI_NAME, SEX, SEX_DIFF,
    TOTAL_LENGTH, VERNACULAR]

ALL_MATCHERS = MATCHERS1 + MATCHERS2

LINKERS = [BODY_PART_LINKER, SEX_DIFF_LINKER]


def trait_pipeline():
    """Setup the pipeline for extracting traits."""
    nlp = spacy.load('en_core_web_sm', exclude=['ner', 'lemmatizer'])
    add_term_ruler_pipe(nlp)
    nlp.add_pipe('merge_entities', name='term_merger')
    nlp.add_pipe('cache_label', after='term_merger')
    add_match_ruler_pipe(nlp)
    add_entity_data_pipe(nlp)
    add_linker_pipe(nlp)
    return nlp


def sentence_pipeline():
    """Setup the pipeline for extracting sentences."""
    nlp = spacy.blank('en')
    add_sentence_term_pipe(nlp)
    nlp.add_pipe('merge_entities')
    add_sentence_pipe(nlp)
    return nlp


def add_term_ruler_pipe(nlp):
    """Add a pipe to identify phrases and patterns as base-level traits."""
    config = {'phrase_matcher_attr': 'LOWER'}
    term_ruler = nlp.add_pipe(
        'entity_ruler', name='term_ruler', config=config, before='parser')
    term_ruler.add_patterns(TERMS.for_entity_ruler())
    add_ruler_patterns(term_ruler, *MATCHERS1)


def add_match_ruler_pipe(nlp):
    """Add a pipe to group tokens into larger traits."""
    config = {'overwrite_ents': True}
    match_ruler = nlp.add_pipe('entity_ruler', name='match_ruler', config=config)
    add_ruler_patterns(match_ruler, *MATCHERS2)


def add_entity_data_pipe(nlp):
    """Add a pipe that adds data to entities."""
    config = {'actions': EntityData.from_matchers(*ALL_MATCHERS)}
    nlp.add_pipe('entity_data', config=config)


def add_linker_pipe(nlp):
    """Add a pipe for linking body parts with other traits."""
    config = {'patterns': LINKERS}
    nlp.add_pipe('dependency', name='body_part_linker', config=config)


def add_sentence_term_pipe(nlp):
    """Add a pipe that adds terms used to split text into sentences."""
    config = {'phrase_matcher_attr': 'LOWER'}
    term_ruler = nlp.add_pipe('entity_ruler', config=config)
    add_ruler_patterns(term_ruler, DOC_HEADING)


def add_sentence_pipe(nlp):
    """Add a sentence splitter pipe."""
    abbrevs = """
        Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
        mm cm m
        """.split()
    config = {'abbrevs': abbrevs, 'headings': ['doc_heading']}
    nlp.add_pipe('sentence', config=config)
