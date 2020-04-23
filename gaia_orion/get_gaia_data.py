import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia
from astroquery.simbad import Simbad


def get_gaia_stars(name, width):
    result_table = Simbad.query_object(name)
    ra, dec = result_table["RA"][0], result_table["DEC"][0]

    coord = SkyCoord(ra=ra, dec=dec, unit=(u.degree, u.degree), frame='icrs')
    r = Gaia.query_object_async(coordinate=coord, width=width, height=width)

    return r

