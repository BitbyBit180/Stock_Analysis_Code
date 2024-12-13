import yfinance as yf
import pandas_ta as ta
from textblob import TextBlob
import streamlit as st

# Function to fetch stock data
def fetch_stock_data(ticker, period="1y"):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        if data.empty:
            st.error(f"No data found for ticker {ticker}. Please check the symbol and try again.")
            return None
        return data
    except Exception as e:
        st.error(f"Error fetching stock data: {e}")
        return None

# Function to calculate indicators
def calculate_indicators(data):
    data['RSI'] = ta.rsi(data['Close'], length=14)
    macd = ta.macd(data['Close'])
    data['MACD'] = macd['MACD_12_26_9']
    data['MACD_signal'] = macd['MACDs_12_26_9']
    return data

# Function to analyze sentiment
def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Function to run the dashboard
