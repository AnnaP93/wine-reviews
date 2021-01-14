import numpy as np
from read_input import wine_reviews as reviews
from countries_variety import get_top_5_popular_wines, get_avg_price_per_type, get_wineries_by_country


def initial_analysis():
    reviews().info()
    print('The dimensions of the datatset are: ', reviews().shape)
    print()
    print(reviews().isnull().sum())
    print("All the columns except 'description', 'points', 'title' and 'winery' include missing values.")
    print()
    print(reviews().describe(include=[np.number]))


def execute():
    print('Initial dataset analysis:')
    initial_analysis()

    print('Top 5 most popular types of wines are:')
    print(get_top_5_popular_wines())

    print("The average prices for each type of the most popular wines are presented below:")
    get_avg_price_per_type()

    print("The number of wineries broken down by countries:")
    print(get_wineries_by_country())


execute()
