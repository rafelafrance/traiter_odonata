"""Build the NLP pipeline."""

import spacy
from traiter.patterns.matcher_patterns import (
    add_ruler_patterns, as_dicts, patterns_to_dispatch)
from traiter.pipes.add_entity_data import ADD_ENTITY_DATA
from traiter.pipes.cache import CACHE_LABEL
from traiter.pipes.cleanup import CLEANUP
# from traiter.pipes.debug import debug_tokens
from traiter.pipes.dependency import DEPENDENCY
from traiter.pipes.sentence import SENTENCE
from traiter.pipes.simple_entity_data import SIMPLE_ENTITY_DATA
from traiter.tokenizer_util import append_abbrevs

from odonata.patterns.body_part import BODY_PART, BODY_SEGMENTS, BODY_SUBPART
from odonata.patterns.color import COLOR
from odonata.patterns.color_like import COLOR_LIKE
from odonata.patterns.color_linker import COLOR_LINKER
from odonata.patterns.color_mod import COLOR_MOD
from odonata.patterns.color_like_linker import COLOR_LIKE_LINKER
from odonata.patterns.color_mod_linker import COLOR_MOD_LINKER
from odonata.patterns.habitat import HABITAT
from odonata.patterns.hind_wing_length import HIND_WING_LENGTH
from odonata.patterns.sci_name import SCI_NAME
from odonata.patterns.sex_life_stage_linker import SEX_LIFE_STAGE_LINKER
from odonata.patterns.term_patterns import DOC_HEADING, RANGE, SEGMENTS
from odonata.patterns.total_length import TOTAL_LENGTH
from odonata.patterns.vernacular import VERNACULAR
from odonata.pylib.const import ABBREVS, FORGET, REPLACE, TERMS

ENTITY_MATCHERS = [
    BODY_PART, BODY_SEGMENTS, BODY_SUBPART, COLOR, COLOR_LIKE, COLOR_MOD,
    HABITAT, HIND_WING_LENGTH, SCI_NAME, TOTAL_LENGTH, VERNACULAR]

LINKERS = [COLOR_LINKER, COLOR_LIKE_LINKER, COLOR_MOD_LINKER]


def pipeline():
    """Setup the pipeline for extracting traits."""
    nlp = spacy.load('en_core_web_sm', exclude=['ner', 'lemmatizer'])
    append_abbrevs(nlp, ABBREVS)

    config = {'phrase_matcher_attr': 'LOWER'}
    term_ruler = nlp.add_pipe(
        'entity_ruler', name='term_ruler', config=config, before='parser')
    term_ruler.add_patterns(TERMS.for_entity_ruler())
    add_ruler_patterns(term_ruler, [DOC_HEADING, RANGE, SEGMENTS])

    nlp.add_pipe(SENTENCE, before='parser')

    nlp.add_pipe('merge_entities', name='term_merger')
    nlp.add_pipe(SIMPLE_ENTITY_DATA, after='term_merger', config={'replace': REPLACE})

    nlp.add_pipe(CACHE_LABEL, after='term_merger')

    config = {'overwrite_ents': True}
    match_ruler = nlp.add_pipe('entity_ruler', name='match_ruler', config=config)
    add_ruler_patterns(match_ruler, ENTITY_MATCHERS)

    config = {'dispatch': patterns_to_dispatch(ENTITY_MATCHERS)}
    nlp.add_pipe(ADD_ENTITY_DATA, config=config)

    nlp.add_pipe(DEPENDENCY, name='linkers', config={'patterns': as_dicts(LINKERS)})
    nlp.add_pipe(SEX_LIFE_STAGE_LINKER)

    nlp.add_pipe(CLEANUP, config={'entities': FORGET})

    # debug_tokens(nlp)

    return nlp
