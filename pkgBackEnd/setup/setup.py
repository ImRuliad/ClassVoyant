import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import requests

from pkgBackEnd.scraper.get_url import get_url_content


def setup_webdriver():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        #chrome_options.page_load_strategy = 'eager'

        web_driver = webdriver.Chrome(options=chrome_options)

    except Exception as e:
        logging.error(f"Some error occurred {e}")

    return web_driver


if __name__ == "__main__":
    web_driver = setup_webdriver()
    get_url_content(web_driver)
    time.sleep(10)

