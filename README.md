# Background Analysis of Wine Reviews Dataset

### Dataset Resources
The dataset used for the analysis was found on Kaggle - https://www.kaggle.com/zynicide/wine-reviews. Originally, the data was scraped from WineEnthusiast - https://www.winemag.com/?s=&drink_type=wine

Please note that there are two datasets presented on the given webpage, but only _winemag-data-130k-v2.csv_ was used. You can download the .csv file either from the webpage or from the _input_ folder under this repository.

### Dataset Details

**__winemag-data-130k-v2.csv__** dataset has 129,971 entries (including column titles row) divided across 13 columns.

The columns of the dataset are listed below:
- country: the country that the wine is from;
- description: description of the wine taste;
- designation: the vineyard within the winery where the grapes that made the wine are from;
- points: the number of points WineEnthusiast rated the wine on a scale of 1-100 
- price: the cost for a bottle of the wine;
- province: the province or state that the wine is from;
- region_1: the wine growing area in a province or state (ie Napa); 
- region_2: Sometimes there are more specific regions specified within a wine growing area (ie Rutherford inside the Napa Valley);
- taster_name: name of the person providing the review;
- taster_twitter_handle: twitter handle of the person providing the review; 
- title: the title of the wine being reviewed; 
- variety: the type of grapes used to make the wine (ie Pinot Noir);
- winery: the winery that made the wine.


### Goal

The goal of this project is to analyze the different types of wines and their reviews with Pandas.

### Program Details

The program provides the following features:

- general overview of the dataset with **initial_analysis()** function. This function returns the shape of the dataset, information on the types of columns and whether any columns include nulls.

- **get_top_5_popular_wines()** returns 5 most-popular wine types in the world (sorted by variety).

- **get_avg_price_per_type()** returns an average price for each type of wine (eg 'The average price per Pinot Noir is $47).

- **get_wineries_by_country()** returns the number of wineries broken down by countries and sorted in the descending order.

- **find_common_wine_producers_and_countries()** returns the most common wine-producing regions broken down by countries and sorted in descending order (The nulls were filtered out into "Unknown" group.)

- **get_max_point_per_province()** showcase the maximum rating score per each province.

- **get_price_extremes()** returns max and min prices for each type of wine.

- **get_min_price_per_point()** returns the cheapest wines for each points category.

- **get_max_points_per_price()** returns the highest_rating wines and their corresponding countries per each price category.

- **get_high_ranking_low_price()** presents a list of highest-rating wines under 50$ that might be valuable for budget wine connoisseurs.

