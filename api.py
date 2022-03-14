import yaml
from fastapi import FastAPI


def create_module():
    with open('config.yaml', 'rt') as f:
        config = yaml.safe_load(f)

    if config['module'] == 'distilbert':
        from modules.bert_sentiment import DistilBERTPredictor
        checkpoint_dir = config['weights']
        module = DistilBERTPredictor(checkpoint_dir)
        return module

    if config['module'] == 'random':
        from modules.random import RandomPredictor
        module = RandomPredictor()
        return module

    raise ValueError(f'Unknow module name = {config["module"]}')


module = create_module()
app = FastAPI()


@app.post('/api/stock-trend')
def news_headlines_stock_trend_prediction(news_headline: str):
    predicted_trend = module.predict(news_headline)
    return {
        'headline': news_headline,
        'predicted_trend': predicted_trend
    }
