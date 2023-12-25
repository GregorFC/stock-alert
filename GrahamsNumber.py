import yfinance as yf
import pandas as pd

def getGrahamsNumber(ticker):
    # Fetch AEX index components
    aex_tickers = yf.Ticker(ticker)
    # print(aex_tickers.info.keys())

    bookValue = aex_tickers.info.get('bookValue')
    EPStrailing = aex_tickers.info.get('trailingEps')
    EPSforward = aex_tickers.info.get('forwardEps')
    price = yf.Ticker(ticker).info.get('regularMarketOpen')

    if (bookValue == None or EPStrailing == None):
        return 0

    d = dict()
    d['ticker'] = ticker
    d['Graham'] = (22.5 * EPStrailing * bookValue)**0.5
    d['GrahamForward'] = (22.5 * EPSforward * bookValue)**0.5
    d['PE'] = price / EPStrailing
    d['Price'] = price
    return d



# make a list of all the tickers
tickers = ['RDSA.AS', 'ASM.AS', 'ABN.AS', 'AKZA.AS', 'ADYEN.AS', 'INGA.AS', 'ASML.AS', 'ASRNL.AS', 'AGN.AS', 'KPN.AS', 'WKL.AS', 'TKWY.AS', 'AD.AS', 'NN.AS', 'DSM.AS', 'UNA.AS', 'MT.AS', 'REN.AS', 'RAND.AS', 'HEIA.AS', 'GLPG.AS', 'URW.AS', 'IMCD.AS', 'PHIA.AS', 'PRX.AS']

# loop through all tickers and get the grahams number
for ticker in tickers:
    price = yf.Ticker(ticker).info.get('regularMarketOpen')

    print (getGrahamsNumber(ticker))