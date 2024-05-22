import os
from constants.constants import STATES


def get_option():

    print("\tWelcome to PyBnB")
    print("--------------------------------")
    print("1. Search by City Name")
    print("2. Search by State Name")
    print("3. Quit")
    print("--------------------------------")

    return input("Please choose an option (1-3): ").strip()


def get_city():
    city = input("City: ").strip().upper()

    # Check input validity

    if city != "":
        return city
    else:
        return ""


def get_state():
    state = input("State (full or abv): ").strip().upper()

    # Check input user quits
    if state == "Q":
        return state

    # Check if abv state
    if state in STATES:
        return state

    # Check if full state
    for key, value in STATES.items():
        if state == value:
            return key

    return ""


def get_user_input():
    """
    Prompt the user to input the option, city, and state.
    """

    city_flag = False
    state_flag = False
    quit_flag = False
    error = ""
    option = ""
    city = ""
    state = ""

    while not quit_flag:

        # Get user option, proceed or quit
        while not (city_flag or state_flag or quit_flag):

            option = get_option()

            os.system("clear")

            if option == "1":
                city_flag = True
            elif option == "2":
                state_flag = True
            elif option == "3":
                quit_flag = True
            else:
                print("**Invalid choice, please try again.**\n")

        if city_flag:

            if error != "":
                print(error)

            print("Enter the following (press 'Q' to return): \n")

            # Get city to look up
            if (city := get_city()) != "":
                city_flag = False

                if error != "":
                    error = ""

                if city != "Q":
                    state_flag = True

                os.system("clear")

            else:
                error = "** Invalid city, please try again. **\n"

        if state_flag:

            if error != "":
                print(error)

            print("Enter the following (press 'Q' to return): \n")

            if option == "1":
                print("City: " + city)

            # Get state to look up
            if (state := get_state()) != "":
                state_flag = False

                if state != "Q":
                    quit_flag = True
                elif option == "1":
                    city_flag = True

                error = ""
            else:
                error = "** Invalid state, please try again. **\n"

        os.system("clear")

    return (option, city, state)
