"""Build the NLP pipeline."""

import spacy
from traiter.patterns import add_ruler_patterns
from traiter.pipes.entity_data import EntityData
import traiter.pipes.cache_label
import traiter.pipes.debug_pipe
import traiter.pipes.dependency_pipe
import traiter.pipes.sentence_pipe

from src.matchers.body_part import BODY_PART
from src.matchers.body_part_linker import BODY_PART_LINKER
from src.matchers.color import COLOR
from src.matchers.doc_heading import DOC_HEADING
from src.matchers.hind_wing_length import HIND_WING_LENGTH
from src.matchers.range import RANGE
from src.matchers.sci_name import SCI_NAME
from src.matchers.sex import SEX
from src.matchers.total_length import TOTAL_LENGTH
from src.matchers.vernacular import VERNACULAR
from src.pylib.consts import ABBREVS, TERMS

ENTITY = [BODY_PART, COLOR, HIND_WING_LENGTH, SCI_NAME, SEX, TOTAL_LENGTH, VERNACULAR]
RETOKENIZE = [DOC_HEADING, RANGE]
MATCHERS = RETOKENIZE + ENTITY


def pipeline():
    """Setup the pipeline and return an nlp object."""
    nlp = spacy.load('en_core_web_sm', exclude=['ner', 'lemmatizer'])

    config = {'abbrevs': ABBREVS, 'headings': ['doc_heading']}
    nlp.add_pipe('sentence', config=config, before='parser')

    # Identify traits in the document
    config = {'phrase_matcher_attr': 'LOWER'}
    term_ruler = nlp.add_pipe(
        'entity_ruler', name='term_ruler', config=config, after='parser')
    term_ruler.add_patterns(TERMS.for_entity_ruler())
    add_ruler_patterns(term_ruler, *RETOKENIZE)

    nlp.add_pipe('merge_entities', name='term_merger', after='term_ruler')

    # Save the current label so that it can be used after another entity_ruler
    nlp.add_pipe('cache_label', after='term_merger')

    nlp.add_pipe('debug_tokens', name='debug1')

    # Group tokens into larger traits
    config = {'overwrite_ents': True}
    match_ruler = nlp.add_pipe('entity_ruler', name='match_ruler', config=config)
    add_ruler_patterns(match_ruler, *ENTITY)

    nlp.add_pipe('debug_tokens', name='debug2')
    nlp.add_pipe('debug_entities', name='debug3')

    # Update the token and span ._.data
    config = {'actions': EntityData.from_matchers(*MATCHERS)}
    nlp.add_pipe('entity_data', config=config)

    config = {
        'label': BODY_PART_LINKER['label'],
        'patterns': BODY_PART_LINKER['patterns'],
        'on_match': 'body_part_linker.v1',
    }
    nlp.add_pipe('dependency', config=config)

    # self.nlp.add_pipe(sex_linker, name=SEX_STEP)

    print(nlp.pipe_names)
    return nlp
