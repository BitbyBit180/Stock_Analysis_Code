import yfinance as yf
import pandas_ta as ta
from textblob import TextBlob
import streamlit as st

# Function to fetch stock data
def fetch_stock_data(ticker, period="1y"):
    stock = yf.Ticker(ticker)
    return stock.history(period=period)

# Function to calculate indicators
def calculate_indicators(data):
    data['RSI'] = ta.rsi(data['Close'], length=14)
    data[['MACD', 'MACD_signal']] = ta.macd(data['Close'])
    return data

# Function to analyze sentiment
def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Function to run the dashboard
def run_dashboard(data):
    st.title("Stock Analysis Dashboard")
    st.line_chart(data['Close'])

# Main function
def main():
    data = fetch_stock_data("RELIANCE.NS")
    data = calculate_indicators(data)
    run_dashboard(data)

if __name__ == "__main__":
    main()
