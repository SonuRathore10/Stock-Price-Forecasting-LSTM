# 📈 Stock Price Forecasting API using LSTM (FastAPI)
A deep learning project for predicting stock closing prices using Long Short-Term Memory (LSTM) networks in TensorFlow/Keras, featuring a FastAPI backend for real-time predictions based on Yahoo Finance data.

## Overview
This project implements a time series forecasting pipeline to predict stock closing prices using historical data from Yahoo Finance. It includes:

- An LSTM-based deep learning model for price prediction.
- Data processing and exploratory analysis.
- A FastAPI backend for serving predictions via HTTP endpoints.
- Support for both historical (actual) and future (predicted) closing prices

### Features
- Automated Data Retrieval: Downloads historical stock data from Yahoo Finance.
- Data Preprocessing: Cleans, normalizes, and sequences data for time series modeling.
- Deep Learning Model: Stacked LSTM with dropout layers for regularization.
- Performance Evaluation: Calculates RMSE and visualizes predictions.
- API Service: FastAPI endpoint for real-time price prediction.
- Handles Both Past and Future Dates: Returns actual prices for past dates, predictions for future dates
