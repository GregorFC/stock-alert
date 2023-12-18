import yfinance as yf
import pandas as pd

def get_aex_symbols():
    # Fetch AEX index components
    aex_tickers = yf.Tickers("^AEX")
    print(aex_tickers)
    # Extract symbols
    aex_symbols = [ticker.info['symbol'] for ticker in aex_tickers.tickers]
    # print(aex_symbols)

    return aex_symbols

def get_aex_stocks():
    # AEX symbols
    aex_symbols = ["ADYEN.AS", "ASML.AS", "DSFIR.AS", "HEIA.AS", "LIGHT.AS", "PHIA.AS", "RAND.AS", "REN.AS", "UNA.AS", "TKWY.AS"]
                    # "DSM.AS", 
    return aex_symbols

def get_high_relative_volume_stocks(threshold=0.5):
    aex_symbols = get_aex_stocks()
    result_stocks = []

    for symbol in aex_symbols:
        # Download stock data
        stock_data = yf.download(symbol)

        # Calculate relative volume (assuming average volume over the last 30 days)
        avg_volume_30days = stock_data['Volume'].rolling(window=90).mean()
        current_volume = stock_data['Volume'].iloc[-1]
        relative_volume = current_volume / avg_volume_30days.iloc[-1]

        # Check if relative volume is greater than the threshold
        if relative_volume > threshold:
            result_stocks.append({
                'Symbol': symbol,
                'RelativeVolume': relative_volume
            })

    return pd.DataFrame(result_stocks)

if __name__ == "__main__":
    # Adjust the threshold as needed
    threshold_value = 0.1

    # Get stocks with high relative volume
    high_relative_volume_stocks = get_high_relative_volume_stocks(threshold=threshold_value)

    # Display the result
    print(f"Stocks with relative volume greater than {threshold_value}:")
    print(high_relative_volume_stocks)