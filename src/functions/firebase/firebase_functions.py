import os
import firebase_admin
import threading
from firebase_admin import credentials, firestore


def firebase_upload(city, state):
    """
    Upload city data to Firebase Database.
    """

    db_ref = firestore.client()
    state_ref = db_ref.collection(state)
    cities_ref = state_ref.document(city["Name"])
    city_ref = cities_ref.get()

    data = {}

    # Check if city exists in DB
    if not city_ref.exists:

        data["city_name"] = city["Name"]
        data["airbnb_rate"] = city["AirBnB Rate"]
        data["growth_rate"] = city["Growth Rate"]
        data["rental_yield"] = city["Rental Yield"]
        data["list_prices"] = city["Listing Prices"]

        cities_ref.set(data, merge=True)
    else:
        airbnb_flag = False
        list_price_flag = False

        city_data = city_ref.to_dict()

        # Check if avg Airbnb rate is up-to-date
        if city_data["airbnb_rate"] != city["AirBnB Rate"]:
            data["airbnb_rate"] = city["AirBnB Rate"]
            airbnb_flag = True

        # Check if median list prices are up-to-date
        if city_data["list_prices"] != city["Listing Prices"]:
            data["list_prices"] = city["Listing Prices"]
            list_price_flag = True

        # Update values in DB
        if airbnb_flag or list_price_flag:
            data["growth_rate"] = city["Growth Rate"]
            data["rental_yield"] = city["Rental Yield"]
            cities_ref.set(data, merge=True)


def upload_data(cities, state):
    """
    Utilizes multithreading to concurrently upload data to a Firebase Database.
    """
    
    try:    
        # Set and initilize Firebase credentials
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./credentials.json"
        cred = credentials.Certificate("./credentials.json")
        firebase_admin.initialize_app(cred)

        threads = []

        for city in cities:
            thread = threading.Thread(target=firebase_upload, args=(city, state))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        return True
    
    except Exception as e:
        return False
