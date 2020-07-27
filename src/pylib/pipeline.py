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

    traits = []

    for token in doc:
        if (token._.step in ('traits', 'headers') and token._.data
                and not token._.aux.get('skip')):
            data = {k: v for k, v in token._.data.items()
                    if not k.startswith('_')}
            data['trait'] = token.ent_type_
            data['start'] = token.idx
            data['end'] = token.idx + len(token)
            traits.append(data)

    sents = []
    for sent in doc.sents:
        sentence_traits(traits, sent)
        sents.append((sent.start_char, sent.end_char))

    # from pprint import pp
    # pp(traits)

    return (traits, sents) if with_sents else traits


def sentence_traits(traits, span):
    """Handle traits that happen at the sentence level."""
    habitat = any(t.ent_type_ == 'habitat' for t in span)
    if habitat:
        traits.append({
            'trait': 'habitat',
            'habitat': span.text,
            'start': span.start_char,
            'end': span.end_char,
        })


def attach(traits):
    """Attach traits to the species."""
    traits = sorted(traits, key=lambda x: x['start'])

    attached = []
    record = []
    has_habitat = True  # Prevent a blank record from being added
    for trait in traits:
        if trait['trait'] in ('sci_name', 'vernacular'):
            continue
        elif trait['trait'] == 'header':
            if record:
                attached.append(record)
            record = [trait]
            has_habitat = False
        elif trait['trait'] == 'habitat' and not has_habitat:
            record.append(trait)
            has_habitat = True
        elif trait['trait'] != 'habitat' and record:
            record.append(trait)

    return attached
