# stock-trend-predictions
Stock trend prediction based on the news headlines

# Introduction

Problem statement:
- Input: a news headline: a string
- Output: a predicted stock trend: an integer `0` or `1`

Project structure:
```
.
├── data
│   ├── daily-financial-news
│   └── huge-stock-market
│       ├── Data
│       │   ├── ETFs
│       │   └── Stocks
│       ├── ETFs
│       └── Stocks
├── modules
├── papers
└── weights
    └── 20220314_distilbert
```

# Installation

```
pip install transformers fastapi torch
```

DistilBert weights: https://drive.google.com/drive/folders/1KFmdF-8GHaY0viOoHxxu-xG-QE_FdLEM?usp=sharing
Download and extract and rename to the same as it is in the project structure above.

# Usage

Run in the terminal:

```
uvicorn api:app --host 0.0.0.0 --port 8000
```

The easiest way to test is to open a browser, e.g., Google Chrome, and enter:
```
http://0.0.0.0:8000/docs
```

Here you can try out some availables API

# Progress

1. Data Preparation (See README in the `data` folder)
1. Model training
- I tried random prediction for the baseline
- I tried fine-tuning DistilBert for classification task where the target is the up/down trend [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1hBRgVoHYwuK_orpYN3s_VxmkeDiH9DAI?usp=sharing)


# Project limited
- I haven't worked on NLP so that it took me a while to understand some terms and research topics.
- Only predict the trend, e.g., upward (1) or downward (0). Don't provide the quantity nor the volumne


# References

- https://huggingface.co/docs/transformers/training
- https://github.com/bentrevett/pytorch-sentiment-analysis/blob/master/1%20-%20Simple%20Sentiment%20Analysis.ipynb
- https://github.com/bentrevett/pytorch-sentiment-analysis/blob/master/6%20-%20Transformers%20for%20Sentiment%20Analysis.ipynb
