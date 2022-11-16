[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)


<div align = center>
<a href = "github.com/plugyawn"><img width="400px" height="400px" src= "https://user-images.githubusercontent.com/76529011/202106478-17b62613-6b4f-4d63-91eb-f1a375de1c45.png"></a>
</div>

-----------------------------------------
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)![Compatibility](https://img.shields.io/badge/compatible%20with-python3.6.x-blue.svg)

```Coinframe``` is a library for backtesting on cryptocurrency portfolios, as well as analyzing correlations, plotting relevant rolling graphs, and more.

With ```coinframe```, you can set portfolios, buy, sell, and check value at every step. Designed to work with all standard cryptocurrency data-sources, ```Coinframe``` allows rapid checking of trading strategies on python, on-the-go. 

## A backtesting example.

Here, we have a ```coinframe``` object named ```cf```, and in the ```coin_list```, we have ```ETH``` and ```SOL```; data has been pooled from the ```data``` directory in the repository.

```python
i = 0
while (i < 1000):
    if rise.loc[rise.index == cf.backtest.index[offset+i]]["Derivative"].values[0] == 1:
        if cf.coin_list["ETH"] >= 1:
            success = cf.sell(1, "ETH")
            if not success:
                continue
        cf.buy(1, "SOL")
    else:
        if cf.coin_list["SOL"] >= 1:
            success = cf.sell(1, "SOL")
        cf.buy(1, "ETH")
    cf.progress(steps = 60)
    print(f"Total money: {cf.money}, Total coins: {cf.coin_list}, Total value: {cf.find_value()}")
    i +=1 
```

```
Coinframe Error: Not enough money to buy. 
 Require 3433.73 but only have 3003.49.
Total money: 3003.49, Total coins: {'Price': 0, 'SOL': 0, 'ETH': 37}, Total value: 130219.85
----------------------------------------
Sell 1 ETH for 3438.28. 
 Now have 36 ETH and 6441.77 money.
Buy 1 SOL for 177.69999999999982. 
 Now have 1 SOL and 6264.070000000001 money.
Total money: 6264.070000000001, Total coins: {'Price': 0, 'SOL': 1, 'ETH': 36}, Total value: 129625.16000000002
----------------------------------------
Sell 1 SOL for 177.73. 
 Now have 0 SOL and 6441.8 money.
Buy 1 ETH for 3421.76. 
 Now have 37 ETH and 3020.04 money.
Total money: 3020.04, Total coins: {'Price': 0, 'SOL': 0, 'ETH': 37}, Total value: 129893.78
```

## A plotting example.

```python
eth_data = pd.read_csv("./data/BitMart/ETH_USDT_5m.csv")
cf = coinframe(eth_data)
cf.rolling_average(hours = HOURS)
cf.coin.plot()
```

<img width="547" alt="image" src="https://user-images.githubusercontent.com/76529011/202109451-98fb0a8c-3bcf-4e36-8c56-8f2d53a13fda.png">

## Future plans

Future plans include visualizing heatmaps and related graphs for finding correlations between coins, and more.

```
sns.clustermap(correlation_matrix, cmap="RdYlGn")
plt.show()
```
<a href = "github.com/plugyawn"><img width="400px" height="400px" src= "https://user-images.githubusercontent.com/76529011/202109880-0fd9c86d-a931-4c31-bc23-fc44566848c7.png"></a>

## Contributing

Coinframe is a work-in-progress, so feel free to put in a PR and share in the work!

Notably, if you can find a way to add backtesting strategies through boolean expressions passed to the function, that would be really helpful!
Reach me at ```progyan.das@iitgn.ac.in``` or ```progyan.me```.

