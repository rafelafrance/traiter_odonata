"""Walk the spaCy parse tree to assign body parts to traits."""


def body_part_walker(doc):
    """Walk the spaCy parse tree to assign body parts to traits."""
    for sent in doc.sents:
        root = sent.root
        walk(root)
    return doc


def walk(token, level=0):
    """Simple recursive tree walker,"""
    print(f'{level} {"  " * level} {token.pos_:<6} {token.ent_type_:<13} '
          f'{token.dep_:<8} {token.text}')
    level += 1
    for child in token.children:
        walk(child, level)
