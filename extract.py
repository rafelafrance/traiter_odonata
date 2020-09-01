#!/usr/bin/env python3

"""Extract src traits from scientific literature (PDFs to text)."""

import csv
from collections import defaultdict

import src.pylib.util as util

MARKERS = util.DATA_DIR / 'Fraser_1933_Fauna_India_Odonata_I_species.txt'
FRASER = util.TXT_DIR / 'Fraser_1933_Fauna_India_Odonata_I.txt'
CSV = util.DATA_DIR / 'Fraser_1933_Fauna_India_Odonata_I.csv'


def main():
    """Extract data from the PDF."""
    with open(MARKERS) as in_file:
        markers = in_file.readlines()
    markers = [m.strip() for m in markers if m]
    markers = [tuple(m.split()) for m in markers]
    markers = set(markers)

    sections = defaultdict(list)
    section = ''
    with open(FRASER) as in_file:
        for line in in_file.readlines():
            line = line.strip()
            key = tuple(line.split())
            if key in markers:
                section = line
            sections[section].append(line)

    with open(CSV, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['species', 'description'])
        for key, lines in sections.items():
            if not key:
                continue
            _, species = key.split(maxsplit=1)
            description = '\n'.join(lines)
            writer.writerow([species, description])


if __name__ == '__main__':
    main()
