import time
import jax.numpy as jnp
import jax
import seaborn as sns
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib
import scipy
import pandas as pd
import numpy as np


def minute_to_epoch(min: float) -> float:
    """
    Converts minutes to epoch time.
    """
    return min*6000


def crosscorr(datax, datay, lag=0, wrap=False):
    """ Lag-N cross correlation. 
    Shifted data filled with NaNs 

    Parameters
    ----------
    lag : int, default 0
    datax, datay : pandas.Series objects of equal length
    Returns
    ----------
    crosscorr : float
    """
    if wrap:
        shiftedy = datay.shift(lag)
        shiftedy.iloc[:lag] = datay.iloc[-lag:].values
        return datax.corr(shiftedy)
    else:
        return datax.corr(datay.shift(lag))


def moving_average_plots(cf: pd.DataFrame, name: Any) -> None:
    """
    Plots an assortment of diagrams showing different moving averages.

    Parameters:
    ----------
    cf: pd.DataFrame
        Dataframe to plot from.

    name: String
        Name to label plots by.
    """

    cf.reset_columns()
    cf.rolling_average(minutes=30)
    cf.rolling_average(minutes=60)
    cf.rolling_average(minutes=120)
    cf.coin.plot()
    plt.title(name)

    cf.reset_columns()
    cf.rolling_average(days=1)
    cf.rolling_average(weeks=1)
    cf.rolling_average(weeks=4, days=2)
    cf.coin.plot()
    plt.title(name)


def rise_or_fall(df: pd.DataFrame, normalize=True) -> None:
    """
    Returns sign for the rise or fall of a coin.
    """
    if normalize:
        return np.sign(df/np.mean(df))
    else:
        return np.sign(df)
