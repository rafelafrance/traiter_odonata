"""Build the NLP pipeline."""

import spacy
from traiter.spacy_nlp import setup_tokenizer
from traiter.trait_pipeline import TraitPipeline

from .util import HEADER_STEP, LINK_STEP, TRAIT_STEP
from ..matchers.matcher import Matcher
from ..pylib.sentencizer import sentencizer


class Pipeline(TraitPipeline):
    """Build a custom traiter pipeline."""

    steps2link = {TRAIT_STEP, HEADER_STEP}

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        super().__init__(self.nlp)

        self.nlp.disable_pipes(['ner'])

        setup_tokenizer(self.nlp)

        self.matcher = Matcher(self.nlp)
        # self.linker = LinkMatcher(self.nlp)

        self.nlp.add_pipe(sentencizer, before='parser')
        self.nlp.add_pipe(self.matcher, last=True)
        # self.nlp.add_pipe(self.linker, last=True, name=LINK_STEP)


PIPELINE = Pipeline()


# NLP = spacy_nlp()
# NLP.add_pipe(sentencizer, before='parser')
#
# MATCHER = Matcher(NLP)
# NLP.add_pipe(MATCHER, after='parser')
# NLP.max_length *= 2
#
#
# def parse(text, with_sents=False):
#     """Parse the traits."""
#     doc = NLP(text)
#
#     traits = []
#
#     for token in doc:
#         if (token._.step in ('traits', 'headers') and token._.data
#                 and not token._.data.get('_skip')):
#             data = {k: v for k, v in token._.data.items()
#                     if not k.startswith('_')}
#             data['trait'] = token.ent_type_
#             data['start'] = token.idx
#             data['end'] = token.idx + len(token)
#             traits.append(data)
#
#     sents = []
#     for sent in doc.sents:
#         sentence_traits(traits, sent)
#         sents.append((sent.start_char, sent.end_char))
#
#     # from pprint import pp
#     # pp(traits)
#
#     return (traits, sents) if with_sents else traits
#
#
# def sentence_traits(traits, span):
#     """Handle traits that happen at the sentence level."""
#     habitat = any(t.ent_type_ == 'habitat' for t in span)
#     if habitat:
#         traits.append({
#             'trait': 'habitat',
#             'habitat': span.text,
#             'start': span.start_char,
#             'end': span.end_char,
#         })
#
#
# def link(traits):
#     """Attach traits to the species."""
#     traits = sorted(traits, key=lambda x: x['start'])
#
#     attached = []
#     record = []
#     has_habitat = True  # Prevent a blank record from being added
#     for trait in traits:
#         if trait['trait'] in ('sci_name', 'vernacular'):
#             continue
#         elif trait['trait'] == 'header':
#             if record:
#                 attached.append(record)
#             record = [trait]
#             has_habitat = False
#         elif trait['trait'] == 'habitat' and not has_habitat:
#             record.append(trait)
#             has_habitat = True
#         elif trait['trait'] != 'habitat' and record:
#             record.append(trait)
#
#     return attached
