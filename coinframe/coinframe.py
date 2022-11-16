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
# %matplotlib inline
# %config InlineBackend.figure_format = 'svg'


sns.set_style('darkgrid')
np.random.seed(42)
#


from typing import Any, Optional
import datetime


class coinframe():
    """
    A coinframe object contains time-series information about the coin across time.


    Parameters
    ----------
    coin_data : float | pd.DataFrame
        Information about the coin across a long period of time.
    """

    def __init__(self, coin_data: pd.DataFrame):
        self.coin_data = coin_data
        coin_data.columns = ["Time", "Price", "Exchange", "X", "Y", "Z"]
        coin_data = coin_data.drop(["Exchange", "X", "Y", "Z"], axis=1)
        self.coin = coin_data
        self.coin.set_index("Time")
        self.start_time = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(self.coin_data["Time"][0]/1000))
        print(self.coin_data["Time"][0])
        print(
            f"""Coin initilialized from {self.start_time}, for {self.coin_data["Time"][len(self.coin_data)-1]/1000 - self.coin_data["Time"][0]/1000} seconds.""")
        print(self.coin.Time[0])
        print("For a more detailed description of the coin-value time series, run the help() method.")
        self.coin['Time'] = [datetime.datetime.fromtimestamp(
            p/1000) for p in self.coin['Time']]
        self.coin = self.coin.set_index(["Time"])
        sns.set()
        self.money = 1000
        self.coin_backtest = self.coin_data[["Time", "Price"]]

    def plot(self) -> None:
        """ 
        Plot the price of the coin across time.
        """
        plt.plot(self.coin_data["Time"], self.coin["Price"])
        plt.show()

    def rolling_average(self, minutes=0, hours=0, days=0, weeks=0) -> pd.DataFrame:
        """
        Add rolling average as a column.
        
        Parameters:
        ----------
        roll: Int
            How long the window-size is for each average.
        """

        minutes = minutes + hours*60 + days*1440 + weeks*10080

        self.coin[f"Roll-{minutes}"] = self.coin['Price'].rolling(
            minutes).mean()

    def derivative(self, rolling=0) -> pd.DataFrame:
        """
        Difference between each row.
        """
        if rolling == 0:
            return self.coin["Price"].diff()
        else:
            try:
                return self.coin[f"Roll-{rolling}"].diff()
            except:
                print("Parameter Error: No such rolling feature in Dataframe.")

    def reset_columns(self) -> pd.DataFrame:
        """
        Remove rolling averages and other columns from the dataframe.
        
        """

        self.coin = self.coin_data[["Time", "Price"]]
        self.coin = self.coin.set_index(["Time"])

    def help(self) -> None:
        """
        Basic help function, need to fill.
        """

        print("Incomplete function, should fill.")

    def add_coin(self, amount: float, coin_name="Price") -> bool:
        """
        Add a certain amount of a coin to the portfolio.
        """
        if self.backtest[coin_name][0] == 0:
            print(f"Coinframe Error: Coin {coin_name} does not exist.")
            return False
        else:
            self.coin_list[coin_name] += amount
            print(
                f"Added {amount} {coin_name}. \n Now have {self.coin_list[coin_name]} {coin_name} and {self.money} money.")
            return True

    def buy(self, amount: float, coin_name="Price") -> bool:
        """
        Buy a certain amount of the coin.
        """
        if self.money < amount*self.backtest[coin_name][0]:
            print(
                f"Coinframe Error: Not enough money to buy. \n Require {amount*self.backtest[coin_name][0]} but only have {self.money}.")
            return False
        else:
            prev_money = self.money
            self.money -= amount*self.backtest[coin_name][0]
            self.coin_backtest["Money"] = self.money
            self.coin_list[coin_name] += amount
            print(
                f"Buy {amount} {coin_name} for {prev_money-self.money}. \n Now have {self.coin_list[coin_name]} {coin_name} and {self.money} money.")
            return True

    def sell(self, amount: float, coin_name="Price") -> bool:
        """
        Sell a certain amount of the coin.
        """
        if self.coin_list[coin_name] < amount:
            print(
                f"Coinframe Error: Not enough coins to sell. \n Require {amount} but only have {self.coin_list[coin_name]}.")
            return False
        self.money += amount*self.backtest[coin_name][0]
        self.coin["Money"] = self.money
        self.coin_list[coin_name] -= amount
        print(
            f"Sell {amount} {coin_name} for {amount*self.backtest[coin_name][0]}. \n Now have {self.coin_list[coin_name]} {coin_name} and {self.money} money.")
        return True

    def find_value(self) -> float:
        """
        Calculate the value of the portfolio.
        """
        self.value = self.money
        for coin in self.coin_list:
            if coin != "Price":
                self.value += self.coin_list[coin]*self.backtest[coin][0]
        return self.value

    def progress_next(self) -> None:
        """
        Progress to the next time step.
        """
        self.backtest = self.backtest[1:]

    def progress(self, steps: int) -> None:
        """
        Progress a certain amount of time steps.
        """
        self.backtest = self.backtest[steps:]

    def init_backtest(self, money=1000) -> None:
        """
        Initialize the backtest.
        """
        self.backtest = self.coin
        self.money = money
        self.coin_list = {}
        key_list = list(self.coin.columns)
        for key in key_list:
            try:
                key_list = key_list.drop(["Price"], axis=1)
            except:
                pass
            self.coin_list[key] = 0
