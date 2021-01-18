import numpy as np
from read_input import wine_reviews as reviews
from countries_variety import get_top_5_popular_wines, get_avg_price_per_type, get_wineries_by_country, \
    find_common_wine_producers_and_countries, get_max_point_per_province
from reviews_and_prices import get_price_extremes, get_min_price_per_point, get_max_points_per_price, \
    get_high_ranking_low_price


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

    print('The most common wine-producing regions sorted by the number of wines produced in each of the regions:')
    print(find_common_wine_producers_and_countries())

    print('Maximum points per province:')
    print(get_max_point_per_province())

    print("The price extremes for each type of wine are presented below:")
    print(get_price_extremes())

    print("The cheapest wines for each points category are:")
    get_min_price_per_point()
    print()

    print('The highest_rating wines and their corresponding countries are presented below for each price category:')
    print(get_max_points_per_price())
    print()

    print('For budget wine connoisseurs, here is a list of highest-rating wines under 50$.')
    get_high_ranking_low_price()
    print()


execute()
