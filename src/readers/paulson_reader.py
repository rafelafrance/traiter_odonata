"""Parse the Paulson 2011 guide."""

from src.pylib import util as util


def paulson_2011():
    """Extract data from Paulson's guide."""
    path = util.TXT_DIR / 'Paulson_E_odonate_guide.txt'
    with open(path) as in_file:
        return in_file.readlines()
