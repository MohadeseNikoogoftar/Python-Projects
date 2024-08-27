import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stt


# Extraction of cryptocurrency price information through api and draw its graph:

def Fetch(Symbol:str, Market:str = 'USD' ):
    URL = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={}&market={}&apikey=M9CYMA6S7IXGV82X&datatype=csv".format(Symbol, Market)

    Columns = ['timestamp','open','high','low','close','volume']
    
    DF = pd.read_csv(URL, sep=',', usecols= Columns, header=0)

    c = DF['close'].to_numpy()
    c=c[::-1].copy()


  # Examining logarithmic charts:

    L = np.log(c)

    return c,L

Ceth, Leth = Fetch('ETH')
Cbtc, Lbtc = Fetch('BTC')

plt.subplot(2,1,1)
plt.plot(Leth, label = 'ETH Closes')
plt.xlabel('Time (Day)')
plt.ylabel('Price ($)')
plt.legend()

plt.subplot(2,1,2)
plt.plot(Lbtc, label = 'BTC Closes')
plt.xlabel('Time (Day)')
plt.ylabel('Price ($)')
plt.legend()
plt.show()

# Investigating the relationship between Bitcoin and Ethereum cryptocurrencies:

Cs = np.polyfit(Lbtc, Leth, 1)
P = np.poly1d(Cs)


plt.scatter(Lbtc, Leth, s = 4)
plt.plot([8,11], [p(8), p(11)], label = 'Linear Regression', linewidth = 1.3, c = 'k')
plt.xlabel(' BTC Price')
plt.ylabel(' ETH Price')
plt.show()


