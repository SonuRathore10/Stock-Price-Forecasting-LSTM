# backend/utils/predict.py
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta

def get_stock_data(stock_code, period = '5y'):
    df = yf.download(stock_code, period=period)
    return df[['Close']]

def predict_price(stock_code, target_date_str, model, time_step=100):
    today = datetime.today().date()
    target_date = pd.to_datetime(target_date_str).date()

    # Download 2 years of data up to today
    start_date = target_date - timedelta(days=365 * 2)
    df = yf.download(stock_code, start=start_date, end=today + timedelta(days=1))

    if df.empty:
        return f"No data available for {stock_code}."

    df.reset_index(inplace=True)
    df['Date'] = df['Date'].dt.date
    close_prices = df[['Date', 'Close']]

    # 🔁 Case 1: If date is in past or today → return actual price from yfinance
    if target_date <= today:
        print("hi")
        # Filter for that exact date
        actual_row = close_prices[close_prices['Date'] == target_date]
        print(actual_row)
        if not actual_row.empty:
            actual_price = actual_row['Close'].values[0]
            print(actual_price)
            return {
                'Stock': stock_code,
                'Date': target_date_str,
                'Price Type': 'Actual',
                'Closing Price': round(actual_price[0], 2)
            }
        else:
            return f"No trading data for {target_date_str} (possibly a holiday or weekend)."

    # Case 2: Future date → predict using model
    # Manual normalization
    min_price = close_prices['Close'].min()
    max_price = close_prices['Close'].max()
    normalized_prices = (close_prices['Close'] - min_price) / (max_price - min_price)

    # Prepare input sequence for prediction
    input_seq = normalized_prices[-time_step:].values.reshape(1, time_step, 1)

    days_to_predict = (target_date - today).days
    for _ in range(days_to_predict):
        pred = model.predict(input_seq, verbose=0)
        input_seq = np.append(input_seq[:, 1:, :], [[[pred[0][0]]]], axis=1)

    predicted_price = pred[0][0] * (max_price - min_price) + min_price

    return {
        'Stock': stock_code,
        'Date': target_date_str,
        'Price Type': 'Predicted',
        'Closing Price': round(predicted_price, 2)
    }