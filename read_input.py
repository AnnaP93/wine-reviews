import pandas as pd


def wine_reviews():
    reviews = pd.read_csv("input/winemag-data-130k-v2.csv", index_col=0)
    return reviews
