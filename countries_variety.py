from read_input import wine_reviews as reviews


def get_unique_wine_types():
    unique_wine = reviews().groupby('variety').variety.count().sort_values(ascending=False)
    return unique_wine

# print(get_unique_wine_types())


def get_top_5_popular_wines():
    unique_types = get_unique_wine_types()
    top_five = unique_types.head(5)
    top_five_wine_list = []
    for wine_name, variety_count in top_five.items():
        top_five_wine_list.append(wine_name)
    return top_five_wine_list

# print(get_top_5_popular_wines())


def get_avg_price_per_type():
    # exclude_na_prices = reviews()[reviews()['price'].notna()]  # not optimal option as it eliminates some categories
    reviews_df = reviews()
    reviews_df.price.fillna(method='bfill', inplace=True)
    avg_price = reviews_df.groupby('variety').price.mean().sort_values(ascending=False)
    for wine_type, agg_variety in get_unique_wine_types().items():
        x = avg_price[wine_type]
        print('{0} - {1}'.format(wine_type, round(x)))


# get_avg_price_per_type()

def get_wineries_by_country():
    winery_volume_by_country = reviews()[["country", "winery"]].groupby(by="country").count().sort_values(by="winery", ascending=False)
    return winery_volume_by_country


# get_wineries_by_country()




