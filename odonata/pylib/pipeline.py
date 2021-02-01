"""Build the NLP trait_pipeline."""

import spacy
from traiter.pattern_util import add_ruler_patterns
from traiter.pipe_util import from_matchers
from traiter.pipes.add_entity_data import ADD_ENTITY_DATA
from traiter.pipes.cache import CACHE_LABEL
from traiter.pipes.debug import DEBUG_ENTITIES, DEBUG_TOKENS
from traiter.pipes.dependency import DEPENDENCY
from traiter.pipes.sentence import SENTENCE

from odonata.patterns.body_part import BODY_PART, SEGMENTS
from odonata.patterns.body_part_linker import BODY_PART_LINKER
from odonata.patterns.color import COLOR
from odonata.patterns.doc_heading import DOC_HEADING
from odonata.patterns.hind_wing_length import HIND_WING_LENGTH
from odonata.patterns.range import RANGE
from odonata.patterns.sci_name import SCI_NAME
from odonata.patterns.sex import SEX
from odonata.patterns.sex_diff import SEX_DIFF, SEX_DIFF_LINKER
from odonata.patterns.total_length import TOTAL_LENGTH
from odonata.patterns.vernacular import VERNACULAR
from odonata.pylib.const import TERMS

DEBUG_COUNT = 0  # Used to rename debug pipes

ENTITY_MATCHERS = [
    BODY_PART, COLOR, HIND_WING_LENGTH, SCI_NAME, SEX, SEX_DIFF,
    TOTAL_LENGTH, VERNACULAR]

LINKERS = [BODY_PART_LINKER, SEX_DIFF_LINKER]


def trait_pipeline():
    """Setup the pipeline for extracting traits."""
    nlp = spacy.load('en_core_web_sm', exclude=['ner', 'lemmatizer'])
    add_term_ruler_pipe(nlp)
    nlp.add_pipe('merge_entities', name='term_merger')
    nlp.add_pipe(CACHE_LABEL, after='term_merger')
    add_match_ruler_pipe(nlp)
    add_entity_data_pipe(nlp)
    nlp.add_pipe(DEPENDENCY, name='linkers', config={'patterns': LINKERS})
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
    term_matchers = [DOC_HEADING, RANGE, SEGMENTS]
    config = {'phrase_matcher_attr': 'LOWER'}
    term_ruler = nlp.add_pipe(
        'entity_ruler', name='term_ruler', config=config, before='parser')
    term_ruler.add_patterns(TERMS.for_entity_ruler())
    add_ruler_patterns(term_ruler, *term_matchers)


def add_match_ruler_pipe(nlp):
    """Add a pipe to group tokens into larger traits."""
    config = {'overwrite_ents': True}
    match_ruler = nlp.add_pipe('entity_ruler', name='match_ruler', config=config)
    add_ruler_patterns(match_ruler, *ENTITY_MATCHERS)


def add_entity_data_pipe(nlp):
    """Add a pipe that adds data to entities."""
    config = {'actions': from_matchers(*ENTITY_MATCHERS)}
    nlp.add_pipe(ADD_ENTITY_DATA, config=config)


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
    nlp.add_pipe(SENTENCE, config=config)


def add_debug_pipes(nlp, message='', tokens=True, entities=False):
    """Add pipes for debugging."""
    global DEBUG_COUNT
    DEBUG_COUNT += 1
    config = {'message': message}
    if tokens:
        nlp.add_pipe(DEBUG_TOKENS, name=f'tokens{DEBUG_COUNT}', config=config)
    if entities:
        nlp.add_pipe(DEBUG_ENTITIES, name=f'entities{DEBUG_COUNT}', config=config)
