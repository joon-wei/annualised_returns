import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date, timedelta

#%%
tickers = ["VOO", "AAPL", "INTC", "TSM", "AMD"]
endDate = date.today()
startDate = endDate - timedelta(days=365)

columns = ["Ticker", "Annualised Return"]

annualised_returns = pd.DataFrame(columns=["Ticker", "Annualised Return"])

for ticker in tickers:
    data = yf.download(ticker, start=startDate, end=endDate)

    if data.empty:
        print(f"Data download failed for {ticker}")
        continue

    logReturns = np.log(data["Adj Close"] / data["Adj Close"].shift(1))
    logReturns = logReturns[1:]
    annualisedReturn = ((logReturns.mean() + 1) ** len(logReturns)) - 1
    new_row = pd.Series({"Ticker": ticker, "Annualised Return": annualisedReturn})
    annualised_returns = pd.concat(
        [annualised_returns, new_row.to_frame().T], ignore_index=True
    )

print(annualised_returns)
