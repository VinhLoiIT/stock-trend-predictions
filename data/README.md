# Data

Structure:
```
data
├── daily-financial-news
└── huge-stock-market
    ├── Data
    │   ├── ETFs
    │   └── Stocks
    ├── ETFs
    └── Stocks
```

where `daily-financial-news` can be downloaded from https://www.kaggle.com/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests
and `huge-stock-market` can be downloaded from https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs

# Pre-processing

Since the task aims to understand how news headlines affect the up and down trends of the stock market, I don't care about a specific stock. I think the problem can be interpreted as, e.g., if I write this news headline, will the stock rise or not.

This problem can be considered as a text classification.

For this task, we need:
- News Headlines
- Date should in 2014 and 2015
- The open/close of the date => We can measure whether it is up (1) / down or not changed (0)

Steps:

1. I filter the news from 2014 to 2015 with `year-filter_data.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/drive/1PqQff3EfaI84CuvrvAppO7UrWwJBuCYd?usp=sharing)
1. I merge the previous result with stock data (open/close price and assign the corresponding labels) with `stock_data.ipynb`. Train/Test split are also applied here [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/drive/1h5SCKEBMBzbBmgYXF8EtUlV45Jhgn0Yy?usp=sharing)
1. In the end, we've got `train.csv` and `test.csv` files
