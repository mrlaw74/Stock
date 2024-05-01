from vnstock import stock_historical_data
import matplotlib.pyplot as plt
import pandas as pd

# Retrieve historical stock data for the last 20 days with hourly resolution
end_date = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
start_date = (pd.Timestamp.now() - pd.Timedelta(days=20)).strftime('%Y-%m-%d %H:%M:%S')

# Extracting only the date part for end_date
end_date = end_date.split()[0]
# Extracting only the date part for start_date
start_date = start_date.split()[0]

data = stock_historical_data(symbol='TCB', start_date=start_date, end_date=end_date, resolution='1H', type='stock', beautify=True, decor=True, source='DNSE')

# Plotting the closing prices
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], marker='o', linestyle='-')

# Adding titles and labels
plt.title('TCB Stock Closing Prices (Last 20 Days)')
plt.xlabel('Date')
plt.ylabel('Closing Price (VND)')

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Displaying the plot
plt.grid(True)
plt.tight_layout()
plt.show()
