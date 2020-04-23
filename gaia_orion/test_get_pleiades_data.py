from astropy.table import Table
from astroquery.simbad import Simbad


def test_stars_are_returned():
    result = Simbad.query_object("ONC")
    assert len(result) > 0
