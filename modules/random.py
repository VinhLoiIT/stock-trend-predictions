import random
from typing import Optional

from .base import StockTrendPredictor


class RandomPredictor(StockTrendPredictor):

    def __init__(self, seed: Optional[int] = None) -> None:
        super().__init__()
        if seed is not None:
            random.seed(seed)

    def predict(self, headline: str) -> int:
        r"""Predict stock trending from the given headline

        Args:
            headline: the news headline

        Returns:
            A prediction, 0 for not-changed or downward trend, 1 for upward trend
        """
        return random.randint(0, 1)
