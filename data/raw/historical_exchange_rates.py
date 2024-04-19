# Import necessary libraries
import yfinance as yf

# Define stock tickers for Apple, Microsoft, and Google
stock_tickers = ["AAPL", "MSFT", "GOOGL"]

#  Fetch historical stock prices for each company
for ticker in stock_tickers:
    # Fetch historical data
    stock_data = yf.download(ticker, start='2020-01-01', end=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    
    # Calculate percentage change
    stock_data['Change_%'] = (stock_data['Close'].diff() / stock_data['Close'].shift(1)) * 100
    
    # Save historical data to CSV file
    stock_data.to_csv(f'../data/raw/{ticker}_historical_stock_prices.csv')

print("Historical data saved to CSV files.")