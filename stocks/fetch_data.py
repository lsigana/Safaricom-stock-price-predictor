import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(start="2012-01-01", end="2022-12-31")
    data.to_csv(f"{ticker}_data.csv")
    return data

if __name__ == "__main__":
    fetch_stock_data("SCOM, SCOM_data.csv")  # Safaricom's ticker symbol
