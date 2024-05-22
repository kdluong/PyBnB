from selenium import webdriver
from constants.constants import AWNING_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element(driver, class_name):
    """
    Set the wait time duration for an element to load in Selenium.
    """

    # Set wait time
    wait = WebDriverWait(driver, 5)

    # Set element
    element = wait.until(
        EC.visibility_of_any_elements_located((By.CLASS_NAME, class_name))
    )

    return element


def fetch_rate(city, state, driver):
    """
    Utilize Selenium to retrieve the avg daily Airbnb rate for the specified city.
    """

    rate = "null"

    try:

        # Launch browser
        driver.get(AWNING_URL + city.replace(" ", "-") + "-" + state)
        driver.set_page_load_timeout(20)

        # Check if avg Airbnb rate is available
        if not driver.find_elements(By.CLASS_NAME, "estimator--heading"):
            button = wait_for_element(driver, "css-1e8t39a")
            button[1].click()

            temp_rate = wait_for_element(driver, "css-1t9cx4l")

            # Append rate if available, else append null
            if not temp_rate[0].text == "":
                rate = int(temp_rate[0].text[1:])

    except Exception as e:
        pass

    return rate


def fetch_airbnb_data(cities, state):
    """
    Retrieve the avg Airbnb rate for each city.
    """

    # Configure headless browser
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chrome_options)

    rates = []

    # Append rates to list, maintaining the order of cities.
    for city in cities:
        rates.append(fetch_rate(city, state, driver))

    driver.quit()
    return rates
