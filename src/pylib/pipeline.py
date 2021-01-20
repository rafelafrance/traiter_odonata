"""Build the NLP trait_pipeline."""

import spacy
from traiter.patterns import add_ruler_patterns
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
from src.pylib.consts import ABBREVS, TERMS

MATCHERS1 = [DOC_HEADING, RANGE, SEGMENTS]

MATCHERS2 = [
    BODY_PART, COLOR, HIND_WING_LENGTH, SCI_NAME, SEX, SEX_DIFF,
    TOTAL_LENGTH, VERNACULAR]

ALL_MATCHERS = MATCHERS1 + MATCHERS2


def trait_pipeline():
    """Setup the pipeline for extracting traits."""
    nlp = spacy.load('en_core_web_sm', exclude=['ner', 'lemmatizer'])

    # Identify traits in the document
    config = {'phrase_matcher_attr': 'LOWER'}
    term_ruler = nlp.add_pipe(
        'entity_ruler', name='term_ruler', config=config, before='parser')
    term_ruler.add_patterns(TERMS.for_entity_ruler())
    add_ruler_patterns(term_ruler, *MATCHERS1)

    nlp.add_pipe('merge_entities', name='term_merger')

    # Save the current label so that it can be used after another entity_ruler
    nlp.add_pipe('cache_label', after='term_merger')

    # nlp.add_pipe('debug_tokens', name='debug1')

    # Group tokens into larger traits
    config = {'overwrite_ents': True}
    match_ruler = nlp.add_pipe('entity_ruler', name='match_ruler', config=config)
    add_ruler_patterns(match_ruler, *MATCHERS2)

    # Update the token and span ._.data
    config = {'actions': EntityData.from_matchers(*ALL_MATCHERS)}
    nlp.add_pipe('entity_data', config=config)

    # nlp.add_pipe('merge_entities', name='entity_merger')

    # nlp.add_pipe('debug_tokens', name='debug2')
    # nlp.add_pipe('debug_entities', name='debug3')

    config = {'patterns': BODY_PART_LINKER}
    nlp.add_pipe('dependency', name='body_part_linker', config=config)

    config = {'patterns': SEX_DIFF_LINKER}
    nlp.add_pipe('dependency', name='sex_diff_linker', config=config)

    # nlp.add_pipe('debug_tokens', name='debug4')
    # nlp.add_pipe('debug_entities', name='debug5')

    # nlp.add_pipe(SEX_STEP)

    # print(nlp.pipe_names)
    return nlp


def sentence_pipeline():
    """Setup the pipeline for extracting sentences."""
    nlp = spacy.blank('en')

    config = {'phrase_matcher_attr': 'LOWER'}
    term_ruler = nlp.add_pipe('entity_ruler', config=config)
    add_ruler_patterns(term_ruler, DOC_HEADING)

    nlp.add_pipe('merge_entities')

    config = {'abbrevs': ABBREVS, 'headings': ['doc_heading']}
    nlp.add_pipe('sentence', config=config)

    # print(nlp.pipe_names)
    return nlp
