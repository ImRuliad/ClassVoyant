import logging
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options


def setup_driver():

    try:
        chrome_options = Options()
        chrome_options.page_load_strategy = "eager" #if some page elements don't load change to "none"
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
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