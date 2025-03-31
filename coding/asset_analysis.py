# filename: asset_analysis.py
import pandas as pd
from datetime import datetime, timedelta
from functions import get_stock_prices, plot_stock_prices

# Step 1: Set the date range for the last 5 years
end_date = '2025-03-30'
start_date = (datetime.strptime(end_date, "%Y-%m-%d") - timedelta(days=5*365)).strftime("%Y-%m-%d")

# Step 2: Get stock prices for NVDA and BTC-USD
stock_symbols = ['NVDA', 'BTC-USD']
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)

# Step 3: Normalize the stock prices
normalized_prices = stock_prices / stock_prices.iloc[0]

# Step 4: Compute the 60-week moving average for normalized prices
moving_average = normalized_prices.rolling(window=60*7, min_periods=1).mean()  # 60 weeks, with daily data

# Print the normalized prices
print("Normalized Prices:\n", normalized_prices)

# Step 5 and 6: Plot and save the figure
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
plt.plot(normalized_prices.index, normalized_prices['NVDA'], label='NVDA Normalized', color='blue')
plt.plot(normalized_prices.index, moving_average['NVDA'], label='NVDA 60-week MA', color='lightblue')
plt.plot(normalized_prices.index, normalized_prices['BTC-USD'], label='BTC-USD Normalized', color='orange')
plt.plot(normalized_prices.index, moving_average['BTC-USD'], label='BTC-USD 60-week MA', color='peachpuff')

plt.title('Normalized Prices and 60-Week Moving Average')
plt.xlabel('Date')
plt.ylabel('Normalized Price')
plt.legend()
plt.savefig('asset_analysis.png')
plt.show()