"""Write output to an HTML file."""

from collections import defaultdict
from datetime import datetime
from itertools import cycle

from jinja2 import Environment, FileSystemLoader

COLOR_COUNT = 14
BACKGROUNDS = cycle([f'bb{i}' for i in range(COLOR_COUNT)])


def html_writer(args, rows):
    """Output the data."""
    colors = trait_colors(rows)

    for row in rows:
        row['text'] = format_text(row, colors)
        row['traits'] = format_traits(row, colors)

    env = Environment(
        loader=FileSystemLoader('./src/writers/templates'),
        autoescape=True)

    template = env.get_template('html_writer.html').render(
        now=datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M'),
        rows=rows)
    args.html_file.write(template)
    args.html_file.close()


def trait_colors(rows):
    """Make tags for HTML colorizing text."""
    backgrounds = defaultdict(lambda: next(BACKGROUNDS))

    for row in rows:
        for trait in row['traits']:
            key = trait['trait']
            if key not in ('heading',):
                _ = backgrounds[key]
    return backgrounds


def format_text(row, colors):
    """Colorize and format the text for HTML."""
    frags = split_by_trait(row)
    spans = []
    for text, trait in frags:
        if not trait:
            spans.append(text)
        else:
            name = trait['trait']
            fields = {k: v for k, v in trait.items()
                      if k not in ('start', 'end', 'trait', 'in_header')}
            title = '' if name in fields else f'{name}: '
            title += ', '.join(f"{k} = {v}" for k, v in fields.items())
            span = f'<span class="{colors[name]}" title="{title}">{text}</span>'
            spans.append(span)
    return ''.join(spans)


def split_by_trait(row):
    """Break the text into an array of trait text fragments."""
    text = row['doc'].text
    frags = []

    prev_end = 0
    for trait in row['traits']:
        start = trait['start']
        end = trait['end']
        if start > prev_end:
            frags.append((text[prev_end:start], None))
        frags.append((text[start:end], trait))
        prev_end = end

    if prev_end < len(text):
        frags.append((text[prev_end:len(text)], None))

    return frags


def format_traits(row, colors):
    """Format the traits for HTML."""
    traits = defaultdict(list)
    for trait in row['traits']:
        name = trait['trait']
        label = f'<span class="{colors[name]}">{name}</span>'
        fields = {k: v for k, v in trait.items()
                  if k not in ('start', 'end', 'trait', 'in_header')}
        data = '' if name in fields else f'{name}: '
        data += ', '.join(f"{k} = {v}" for k, v in fields.items())
        traits[label].append(data)

    return sorted([(k, '<br/>'.join(v)) for k, v in traits.items()])
