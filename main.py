from fastapi import FastAPI, Query
from tensorflow.keras.models import load_model
from predict import predict_price
import os

app = FastAPI()

# Load the model
model = load_model("/Users/sonurathore/Downloads/Stock_pred/lstm_model.keras")

@app.post(
    "/predict",
    summary="Predict Stock Price",
    description="""
**Predicts the closing stock price for a given company based on user-specified parameters.**

**Query Parameters**:
- `stock_code`: Stock ticker symbol (e.g., AAPL, GOOG)
- `date`: Date for prediction in YYYY-MM-DD format

**Returns**:
- JSON with the predicted closing price for the selected date
"""
)
def get_prediction(
    stock_code: str = Query(..., description="Stock ticker symbol (e.g., AAPL, GOOG)"),
    date: str = Query(..., description="Date for prediction in YYYY-MM-DD format")
):
    predicted = predict_price(stock_code, date, model)
    if predicted is None:
        return {"error": "Not enough historical data for prediction."}
    
    return {
        "stock": stock_code.upper(),
        "predicted_price": predicted,
        "date": date
    }