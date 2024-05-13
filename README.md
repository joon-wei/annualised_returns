# Calculate annualised returns
Simply put the tickers you want in the tickers list and run.

It gathers past 1 year daily returns data (from yahoo finance) to calculate the annualised return and presents it in a simple format. Could be useful for comparing differnt assets and planning your next portfolio. Hopefully the formula is correct, please help me check it lolol

<img src = "https://github.com/joon-wei/annualised_returns/assets/168265734/af98c2a1-8d0d-4f7f-8e4d-83a360cd14a0"> 

<br/><br/>
Requires yfinance module. Install with:
```
pip install yfinance

# on windows cmd I usually use:

python -m pip install yfinance
```

## About 'yfinance'
yfinance seems to currently be the best and easiest way to obtain financial data easily on python. pandas_datareader is also good as it integrates with pandas framework for dataframe manipulation, but its get_data_yahoo function does not work well now (supposedly after yahoo website changed their formatting). 

Cool thing about yfinance is it comes with a function to override pandas_datareader so that you can continue to use it normally with a working yahoo database function. 

```
import pandas_datareader as pdr
yfinance.pdr_override()
```

Of course I did not do that as yfinance works great on its own too. Heres hoping it doesnt break 😌
