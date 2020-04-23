from astropy import units as u
from matplotlib import pyplot as plt

from jupyter_to_pycharm.gaia_orion.get_gaia_data import get_gaia_stars


def plot_stars_and_trails(tbl, years=10):
    """
    Plots the positions of stars and a trail for their proper motions

    Parameters
    ----------
    tbl : astropy.Table
        Results from ``get_gaia_stars()``
    years : float
        Number of years to extend the trail

    """
    mas_to_deg = u.mas.to(u.deg)

    size = tbl["phot_g_mean_mag"]
    x, y = tbl["ra"], tbl["dec"]
    dx, dy = tbl["pmra"] * mas_to_deg, tbl["pmdec"] * mas_to_deg
    dx *= years
    dy *= years

    plt.scatter(x, y, s=size, c="orange")
    for i in range(len(x)):
        plt.plot([x, x-dx], [y, y-dy])

    plt.xlabel("RA [deg]")
    plt.ylabel("Dec [deg]")

    plt.savefig("stars_and_trails.png", format="png")
    plt.savefig("stars_and_trails.pdf", format="pdf")


tbl = get_gaia_stars("ONC", width=0.2*u.deg)
plot_stars_and_trails(tbl=tbl, years=3000)
