def price_growth_rate(initial_list_price, current_list_price):
    """
    Compute the annual growth rate of the property over a 12-month period.
    """

    # Calculate Price Growth Rate (past 12 months)
    intial = int(initial_list_price)
    current = int(current_list_price)

    return str(format(((current - intial) / intial) * 100, ".2f")) + "%"


def gross_rental_yield(airbnb_rate, current_list_price):
    """
    Compute the potential return on investment if the property were rented out.
    """

    # Calculate Potential Annual Rental Income
    annual_rent = airbnb_rate * 365

    # Calculate Gross Rental Yield
    return str(format((annual_rent / int(current_list_price)) * 100, ".2f")) + "%"
