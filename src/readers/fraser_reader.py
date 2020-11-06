"""Parse the Fraser 1933 guide."""

# TODO This is not a reader yet.

import csv
from collections import defaultdict

from src.pylib import util as util


def fraser_1933():
    """Extract data from Fraser's guide."""
    fraser_markers = (util.DATA_DIR
                      / 'Fraser_1933_Fauna_India_Odonata_I_species.txt')
    fraser = util.TXT_DIR / 'Fraser_1933_Fauna_India_Odonata_I.txt'
    fraser_csv = util.DATA_DIR / 'Fraser_1933_Fauna_India_Odonata_I.csv'

    with open(fraser_markers) as in_file:
        markers = in_file.readlines()
    markers = [m.strip() for m in markers if m]
    markers = [tuple(m.split()) for m in markers]
    markers = set(markers)

    sections = defaultdict(list)
    section = ''
    with open(fraser) as in_file:
        for line in in_file.readlines():
            line = line.strip()
            key = tuple(line.split())
            if key in markers:
                section = line
            sections[section].append(line)

    with open(fraser_csv, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['species', 'description'])
        for key, lines in sections.items():
            if not key:
                continue
            _, species = key.split(maxsplit=1)
            description = '\n'.join(lines)
            writer.writerow([species, description])
