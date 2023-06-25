import yfinance as yf
import mplfinance as mpf
import pandas as pd

import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Data Extraction
def extract_historical_data(symbol):
    try:
        # Get historical data using yfinance
        stock = yf.Ticker(symbol)
        data = stock.history(period="1y")
        dfdata=pd.DataFrame(data)
        print(dfdata.head)
        return data
    except Exception as e:
        print("An error occurred during data extraction:", str(e))

# Step 2: Data Processing
def calculate_average_volume(data):
    try:
        # Calculate average daily trading volume
        average_volume = data['Volume'].mean()
        return average_volume
    except Exception as e:
        print("An error occurred during data processing:", str(e))

# Step 3: Data Visualization
def visualize_stock_performance(data,chart_symbol):
    
    try:
        # Create candlestick chart using Plotly
        fig = go.Figure(data=[go.Candlestick(x=data.index,
                                             open=data['Open'],
                                             high=data['High'],
                                             low=data['Low'],
                                             close=data['Close'])])
        fig.update_layout(title='Stock Performance',
                          xaxis_title='Date',
                          yaxis_title='Price')
        fig.show()
    except Exception as e:
        print("An error occurred during data visualization:", str(e))

    try:
        # Create candlestick chart using mplfinance
        mpf.plot(data, type='candle', volume=True, style='yahoo')
        plt.title('Stock Performance')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.show()
    except Exception as e:
        print("An error occurred during data visualization:", str(e))

    try:
        # Create candlestick chart using seaborn
        plt.figure(figsize=(10, 6))
        sns.set(style='whitegrid')
        sns.lineplot(data=data[['Open', 'Close']], palette='tab10', linewidth=2)
        sns.scatterplot(data=data[['High', 'Low']], color='black', marker='o', s=100)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Stock Performance')
        plt.legend(['Open', 'Close', 'High', 'Low'])
        plt.show()
    except Exception as e:
        print("An error occurred during data visualization:", str(e))


if __name__ == '__main__':
    # Define the stock symbol (e.g., 'AAPL' for Apple Inc.)

    symbol = 'AAPL'
    # Step 1: Data Extraction
    data = extract_historical_data(symbol)
    # Step 2: Data Processing
    if data is not None:
        average_volume = calculate_average_volume(data)
        print("Average daily trading volume:", average_volume)
        
        # Step 3: Data Visualization
        visualize_stock_performance(data)
