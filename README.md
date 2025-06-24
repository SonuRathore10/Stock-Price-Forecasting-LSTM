# 📈 Stock Price Forecasting API using LSTM (FastAPI)
A deep learning project for predicting stock closing prices using Long Short-Term Memory (LSTM) networks in TensorFlow/Keras, featuring a FastAPI backend for real-time predictions based on Yahoo Finance data.

## 🧠 Overview
This project implements a time series forecasting pipeline to predict stock closing prices using historical data from Yahoo Finance. It includes:

- An LSTM-based deep learning model for price prediction.
- Data processing and exploratory analysis.
- A FastAPI backend for serving predictions via HTTP endpoints.
- Support for both historical (actual) and future (predicted) closing prices

## ✨ Features
- Automated Data Retrieval: Downloads historical stock data from Yahoo Finance.
- Data Preprocessing: Cleans, normalizes, and sequences data for time series modeling.
- Deep Learning Model: Stacked LSTM with dropout layers for regularization.
- Performance Evaluation: Calculates RMSE and visualizes predictions.
- API Service: FastAPI endpoint for real-time price prediction.
- Handles Both Past and Future Dates: Returns actual prices for past dates, predictions for future dates

## 🗂️ Project Structure
```
.
├── lstm_model_keras.py     # Model training and analysis script
├── main.py                 # FastAPI app (exposes /predict endpoint)
├── predict.py              # Data fetching + prediction logic
├── lstm_model.keras        # Pre-trained LSTM model file
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```
---

## 🛠️ Tech Stack

| Category         | Tools & Libraries         |
|------------------|---------------------------|
| Language         | Python 3.10+              |
| Web Framework    | FastAPI                   |
| ML Framework     | TensorFlow / Keras        |
| Data Processing  | Pandas, NumPy             |
| Data Source      | yfinance (Yahoo Finance)  |
| Deployment       | Uvicorn (ASGI Server)     |

---

## ⚙️ Setup & Installation

1. **Clone the repository**

```
git clone https://github.com/yourusername/stock-lstm-predictor.git
cd stock-lstm-predictor 
```

2. **Install dependencies**
```
pip install -r requirements.txt
```

3. **Train the LSTM Model**

- Run lstm_model_keras.py to:
- Download stock data (default: Tesla, "TSLA")
- Analyze and visualize trends, returns, and volatility
- Train and evaluate the LSTM model
- Save the trained model as lstm_model.keras

4. **Start the API**

```
uvicorn main:app --reload
```

5. **Get a prediction**

- Use an API tool or browser to POST to /predict with parameters:
  - stock_code: e.g. TSLA
  - date: e.g. 2025-07-01
    
Example using curl:
```
curl -X POST "http://localhost:8000/predict?stock_code=TSLA&date=2025-07-01"
```

## 🔌 API Usage

Predict Stock Price
Endpoint: POST /predict

Parameters (as query):
  - stock_code: Stock ticker symbol (e.g., TSLA, AAPL)
  - date: Date for prediction in YYYY-MM-DD format

Response:

- For past/today: Returns actual closing price from Yahoo Finance.
- For future: Returns predicted price from the LSTM model.

Sample JSON Output:
```
{
  "stock": "TSLA",
  "predicted_price": 742.15,
  "date": "2025-07-01"
}
```
## 🚀 Working Prototype
Example: Predicting AAPL Stock Price

<table>
  <tr>
    <th style="text-align:center;">📥 Input</th>
    <th style="text-align:center;">📤 Response</th>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/59bf359e-b94c-4594-a8a5-c88f2026135c" alt="Input" width="100%">
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/0d0580e2-f8c1-4c2f-ba24-1c7007facb87" alt="Response" width="100%">
    </td>
  </tr>
</table>

## 📈 What You’ll Learn

- Working with raw data and cleaning it for modeling
- Normalizing and structuring time-series data
- Building and training an LSTM deep learning model
- Creating a REST API using FastAPI
- Serving ML models for real-time inference
 
## 🚀 Future Extensions

• Integrate Transformer-based models for improved predictions  
• Add financial news sentiment using NLP (e.g., FinBERT)  
• Enable email/SMS alerts for prediction thresholds  
• Add a backtesting module for strategy evaluation  
• Secure API with JWT authentication and rate limiting  

## ⚠️ Disclaimer
Important: Stock price prediction is inherently uncertain. This application should not be used for making financial decisions.
