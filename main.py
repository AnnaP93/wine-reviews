import numpy as np
import pandas as pd

reviews = pd.read_csv("input/winemag-data-130k-v2.csv", index_col=0)
reviews.info()
print(reviews.isnull().sum())
print(reviews.describe(include=[np.number]))
      
