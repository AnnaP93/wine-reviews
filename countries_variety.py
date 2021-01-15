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


def find_common_wine_producers():
    filling_na_in_region_1 = reviews().region_1.fillna("Unknown")
    count_regions = filling_na_in_region_1.groupby(filling_na_in_region_1.values).count().sort_values(ascending=False)
    return count_regions

# print(find_common_wine_producers())


def find_common_wine_producers_and_countries():
    # how it should look:
    # Region (Country): Wine Count
    # Unknown (): 21247
    # Napa Valley (US): 4480
    # Columbia Valley (WA) (Canada): 4124
    # .....
    reviews_copy = reviews()
    reviews_copy.region_1.fillna("Unknown", inplace=True)
    # print(reviews_copy.region_1.isnull().sum())
    region_country = reviews_copy.groupby('region_1').apply(lambda x: x.country.iloc[0])
    if region_country.loc['Unknown']:
        region_country.loc['Unknown'] = ''

    for element in find_common_wine_producers().items():
        region = element[0]
        count = element[1]
        print('{0} ({1}): {2}'.format(region, region_country[region], count))


# find_common_wine_producers_and_countries()


def get_max_point_per_province():
    max_points = reviews().groupby(['country', 'province']).apply(lambda df: df.points.loc[df.points.idxmax()])
    return max_points.sort_values(ascending=False)

# print(get_max_point_per_province())

