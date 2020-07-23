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

    sents = []

    for token in doc:
        if (token._.step in ('traits', 'headers') and token._.data
                and not token._.aux.get('skip')):
            data = {k: v for k, v in token._.data.items()
                    if not k.startswith('_')}
            data['trait'] = token.ent_type_
            data['start'] = token.idx
            data['end'] = token.idx + len(token)
            traits.append(data)

    # from pprint import pp
    # pp(traits)

    return (traits, sents) if with_sents else traits


def attach(traits):
    """Attach traits to the species."""
    traits = sorted(traits, key=lambda x: x['start'])

    attached = []
    record = defaultdict(list)
    for trait in traits:
        if trait['trait'] in ('sci_name', 'vernacular'):
            continue
        elif trait['trait'] == 'header':
            if record:
                attached.append(record)
            record = defaultdict(list)
            record['sci_name'].append(trait['sci_name'])
            record['vernacular'].append(trait['vernacular'])
        else:
            key = trait['trait']
            new_key = key
            i = 1
            while new_key in record:
                i += 1
                new_key = f'{key}_{i}'
            value = {k: v for k, v in trait.items() if k != 'trait'}
            record[new_key].append(value)

    return attached
