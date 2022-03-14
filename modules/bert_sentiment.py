import torch
from transformers import (DistilBertForSequenceClassification,
                          DistilBertTokenizerFast, pipeline)

from .base import StockTrendPredictor


class DistilBERTPredictor(StockTrendPredictor):

    def __init__(self, checkpoint_dir: str) -> None:
        super().__init__()
        tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')
        model = DistilBertForSequenceClassification.from_pretrained(checkpoint_dir)
        self.classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    def predict(self, headline: str) -> int:
        r"""Predict stock trending from the given headline

        Args:
            headline: the news headline

        Returns:
            A prediction, 0 for not-changed or downward trend, 1 for upward trend
        """
        with torch.no_grad():
            pred = self.classifier(headline)[0]
            prediction = int(pred['label'].split('_')[-1])
            return prediction
