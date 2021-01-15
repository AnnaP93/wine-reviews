from read_input import wine_reviews as reviews
import pandas as pd


def get_price_extremes():
    price_extremes = reviews().groupby('variety').price.agg([max, min])
    return price_extremes

# print(get_price_extremes())


def get_min_price_per_point():
    min_price_by_points = reviews().groupby('points').price.min()
    titles_prices_by_points = reviews().groupby(['points', 'price']).apply(lambda df: df.title.iloc[0])
    for points_to_price in min_price_by_points.items():
        print('{0} - {1}'.format(points_to_price, titles_prices_by_points[points_to_price]))

# get_min_price_per_point()


def get_max_points_per_price():
    data = []
    max_points_per_price = reviews().groupby(['price']).points.max()
    points_title_country_per_price = reviews().groupby(['price', 'points']).apply(lambda x: (x.title.iloc[0],
                                                                                             x.country.iloc[0]))
    for price, points in max_points_per_price.items():
        columns = ['price', 'points', 'title', 'country']
        title_and_country = points_title_country_per_price[(price, points)]
        values = (price, points, title_and_country[0], title_and_country[1])
        zipped = zip(columns, values)
        a_dictionary = dict(zipped)
        data.append(a_dictionary)

    new_df = pd.DataFrame(data).set_index(['price', 'points'])
    return new_df

#print(get_max_points_per_price())


def get_high_ranking_low_price():
    df: pd.DataFrame = get_max_points_per_price()
    for index in df.index:
        if index[1] > 95 and index[0] <= 50:
            row = df.loc[index]
            print('price: {0}; points: {1} - {2} - {3}'.format(index[0], index[1], row.title, row.country))


# get_high_ranking_low_price()



