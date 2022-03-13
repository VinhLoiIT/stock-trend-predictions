from fastapi import FastAPI

from modules.random import RandomPredictor

module = RandomPredictor()
app = FastAPI()


@app.post('/api/stock-trend')
def news_headlines_stock_trend_prediction(news_headline: str):
    predicted_trend = module.predict(news_headline)
    return {
        'headline': news_headline,
        'predicted_trend': predicted_trend
    }
