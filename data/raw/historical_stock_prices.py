# Import necessary libraries
import yfinance as yf

# Fetch historical USD to EGP exchange rate data
usd_to_egp_data = yf.download('EGP=X', start='2020-01-01', end='2024-04-14')  # Adjust start and end dates as needed

# Save the data to a CSV file
usd_to_egp_data.to_csv('../data/raw/USD_to_EGP_exchange_rate.csv')
