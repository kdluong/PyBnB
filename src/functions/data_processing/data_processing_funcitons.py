import locale
from constants.constants import STATES
from functions.calculations.calculations import *

def currency_format(amount):
    locale.setlocale(locale.LC_ALL, '')
    return locale.currency(amount, grouping=True)

def print_data(cities, state):
    print(f"\n{STATES[state]} Results:\n")

    print(f"\t{'City':<18}{'Avg List Price':<18}{'Avg AirBnB Rate':<19}{'Property Growth Rate':<24}{'Gross Rental Yield'}")
    print("\t" + "-" * 100 + "\n")
    
    for city in cities:        
        print(f"\t{city["Name"]:<18}"
              f"{list(city["Listing Prices"].values())[0]:<18}"
              f"{city["AirBnB Rate"]:<19}"
              f"{city["Growth Rate"]:<24}"
              f"{city["Rental Yield"]}")

def fetch_list_prices(city, dates):
    """
    Return Provide the median list prices over the past 12 months.
    """

    list_prices = {}

    for i in range(12):
        index = (i + 1) * -1
        list_prices[dates[index]] = currency_format(int(city[index]))

    return list_prices


def process_data(zillow_data, airbnb_data):
    """
    Aggregate city data into dictionaries containing name, rates, calculations, and 12 months of listing prices.
    """

    cities = []

    for city, rate in zip(zillow_data.itertuples(index=False), airbnb_data):
        if rate != "null":
            cities.append(
                {
                    "Name": city[0],
                    "AirBnB Rate": currency_format(rate),
                    "Growth Rate": price_growth_rate(city[-12], city[-1]),
                    "Rental Yield": gross_rental_yield(rate, city[-1]),
                    "Listing Prices": fetch_list_prices(city, zillow_data.columns),
                }
            )

    return cities
