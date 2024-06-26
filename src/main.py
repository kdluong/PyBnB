import os
from functions.zillow.zillow_functions import fetch_zillow_data
from functions.airbnb.airbnb_functions import fetch_airbnb_data
from functions.user_input.user_input_functions import get_user_input
from functions.firebase.firebase_functions import check_credentials, upload_data
from functions.data_processing.data_processing_funcitons import process_data, print_data


def main():

    # Attempt to initilize Firebase credentials
    credentials_exists = check_credentials()

    quit_flag = False

    while not quit_flag:

        # Fetch option, city, and state
        user_input = get_user_input()

        if user_input[0] != "3":
            # Fetch Zillow city/state data
            zillow_data = fetch_zillow_data(user_input[1], user_input[2])

            # Check if city/state exists in Zillow dataset
            if user_input[0] == "1" and len(zillow_data) < 1:
                print("*** Unable to find city, please try again. ***\n")
            else:
                print("1 of 5: Imported data from Zillow.")
                # Scrape real-time Airbnb rates
                print("2 of 5: Fetching real-time AirBnB rates...")
                airbnb_data = fetch_airbnb_data(
                    zillow_data["RegionName"], user_input[2]
                )

                # Clean/Manipulate & Calculate Data
                print("3 of 5: Processing data...")
                processed_data = process_data(zillow_data, airbnb_data)

                # Upload Data to Firebase
                if credentials_exists:
                    print("4 of 5: Uploading data...")

                    if not upload_data(processed_data, user_input[2]):
                        print("Upload skipped, Firebase credentials are not valid.")
                else:
                    print("4 of 5: Upload skipped, Firebase credentials are not found.")

                # Print Results to Console
                print("5 of 5: Printing data...")
                print_data(processed_data, user_input[2])

            if (
                input("\nPress ENTER to continue ('Q' to quit): ").strip().upper()
                == "Q"
            ):
                quit_flag = True
            else:
                os.system("clear")

        else:
            quit_flag = True


if __name__ == "__main__":
    main()
