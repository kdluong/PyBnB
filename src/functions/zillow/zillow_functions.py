import os
import pandas as pd


def fetch_zillow_data(city, state):
    """
    Import Zillow dataset and clean/maniupulate data.
    """

    current_directory = os.path.dirname(__file__)

    # Construct the full path to the CSV file
    csv_file_path = os.path.join(current_directory, "../../data/zillow_data.csv")

    # Read the CSV file using pd.read_csv
    df = pd.read_csv(csv_file_path)

    # Exclude cities not in state
    filtered_df = df.loc[df["StateName"] == state]

    # Filter one more time if city
    if city != "":
        filtered_df = filtered_df.loc[
            filtered_df["RegionName"].str.upper() == city + ", " + state
        ]

        if len(filtered_df) < 1:
            return []

    # Keep columns w/ city names & median list prices from the past 12 months
    cities = pd.concat([filtered_df.iloc[:, 2], filtered_df.iloc[:, -12:]], axis=1)

    # Remove rows w/ null, duplicates, and convert to uppercase
    cities.dropna(inplace=True)
    cities.drop_duplicates(inplace=True)
    cities["RegionName"] = cities["RegionName"].str[:-4].str.upper()

    return cities
