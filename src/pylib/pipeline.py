"""Build the NLP pipeline."""

from collections import defaultdict

from traiter.spacy_nlp import spacy_nlp  # pylint: disable=import-error

from .segmenter import sentencizer
from ..matchers.matcher import Matcher

NLP = spacy_nlp(disable=['ner'])
NLP.add_pipe(sentencizer, before='parser')

MATCHER = Matcher(NLP)
NLP.add_pipe(MATCHER, after='parser')
NLP.max_length *= 2


def parse(text, with_sents=False):
    """Parse the traits."""
    doc = NLP(text)

    traits = defaultdict(list)

    sents = []

    description = {}
    for sent in doc.sents:
        sents.append((sent.start, sent.end))
        if sent[0].ent_type_ == 'header':
            if description.get('sci_name'):
                traits['description'].append(description)
            description = {
                'sci_name': sent[0]._.data['sci_name'],
                'vernacular': sent[0]._.data['vernacular'],
                'description': sent[1:].text,
            }
        elif description.get('description'):
            description['description'] += sent.text

    # for token in doc:
    #     label = token.ent_type_
    #     data = token._.data
    #     if (token._.step in ('traits', ) and token._.data
    #             and not token._.aux.get('skip')):
    #         data = {k: v for k, v in token._.data.items()
    #                 if not k.startswith('_')}
    #         data['start'] = token.idx
    #         data['end'] = token.idx + len(token)
    #         traits[token._.label].append(data)

    # from pprint import pp
    # pp(dict(traits))

    return (traits, sents) if with_sents else traits
