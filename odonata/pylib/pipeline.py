"""Build the NLP trait_pipeline."""

import spacy
from traiter.pattern_util import add_ruler_patterns
from traiter.pipes.add_entity_data import ADD_ENTITY_DATA
from traiter.pipes.cache import CACHE_LABEL
from traiter.pipes.debug import DEBUG_ENTITIES, DEBUG_TOKENS
from traiter.pipes.dependency import DEPENDENCY
from traiter.tokenizer_util import append_abbrevs
from traiter.pipes.sentence import SENTENCE

from odonata.patterns.body_part import BODY_PART, SEGMENTS
from odonata.patterns.body_part_linker import BODY_PART_LINKER
from odonata.patterns.color import COLOR
from odonata.patterns.doc_heading import DOC_HEADING
from odonata.patterns.hind_wing_length import HIND_WING_LENGTH
from odonata.patterns.range import RANGE
from odonata.patterns.sci_name import SCI_NAME
from odonata.patterns.sex import SEX
from odonata.patterns.sex_diff import SEX_DIFF
from odonata.patterns.sex_diff_linker import SEX_DIFF_LINKER
from odonata.patterns.total_length import TOTAL_LENGTH
from odonata.patterns.vernacular import VERNACULAR
from odonata.pylib.const import ABBREVS, TERMS

DEBUG_COUNT = 0  # Used to rename debug pipes

ENTITY_MATCHERS = [
    BODY_PART, COLOR, HIND_WING_LENGTH, SCI_NAME, SEX, SEX_DIFF,
    TOTAL_LENGTH, VERNACULAR]

LINKERS = [BODY_PART_LINKER, SEX_DIFF_LINKER]


def trait_pipeline():
    """Setup the pipeline for extracting traits."""
    nlp = spacy.load('en_core_web_sm', exclude=['ner', 'lemmatizer'])
    append_abbrevs(nlp, ABBREVS)

    config = {'phrase_matcher_attr': 'LOWER'}
    term_ruler = nlp.add_pipe(
        'entity_ruler', name='term_ruler', config=config, before='parser')
    term_ruler.add_patterns(TERMS.for_entity_ruler())
    add_ruler_patterns(term_ruler, DOC_HEADING, RANGE, SEGMENTS)

    nlp.add_pipe('merge_entities', name='term_merger')

    nlp.add_pipe(CACHE_LABEL, after='term_merger')

    config = {'overwrite_ents': True}
    match_ruler = nlp.add_pipe('entity_ruler', name='match_ruler', config=config)
    add_ruler_patterns(match_ruler, *ENTITY_MATCHERS)

    config = {'patterns': ENTITY_MATCHERS}
    nlp.add_pipe(ADD_ENTITY_DATA, config=config)

    nlp.add_pipe(DEPENDENCY, name='linkers', config={'patterns': LINKERS})

    return nlp


def add_debug_pipes(nlp, message='', tokens=True, entities=False):
    """Add pipes for debugging."""
    global DEBUG_COUNT
    DEBUG_COUNT += 1
    config = {'message': message}
    if tokens:
        nlp.add_pipe(DEBUG_TOKENS, name=f'tokens{DEBUG_COUNT}', config=config)
    if entities:
        nlp.add_pipe(DEBUG_ENTITIES, name=f'entities{DEBUG_COUNT}', config=config)
