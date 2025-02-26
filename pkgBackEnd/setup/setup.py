import logging
from selenium import webdriver
from selenium.common import WebDriverException


def setup_driver():

    try:
        driver = webdriver.Chrome()
        return driver
    except FileNotFoundError:
        logging.error(f"A path to Chrome Webdriver was not found.")
        logging.error(f"Please ensure a Chrome WebDriver is downloaded and path is correctly set.")
    except WebDriverException:
        logging.error(f"A problem occurred with the initialization of the webdriver.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    driver = setup_driver()