import yahoo_finance

from yahoo_finance import Share

yahoo = Share('YHOO')

yahoo.get_open()

print(yahoo.get_open())

import yfinance as yf

msft = yf.Ticker("MSFT")
print(msft)

msft.info
