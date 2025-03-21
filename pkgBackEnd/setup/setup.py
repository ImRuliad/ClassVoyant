import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pkgBackEnd.scraper.get_url import get_url_content



"""
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
"""


class WebDriverManager:
    def __init__(self, headless=True, disable_gpu=True, page_load_strategy='eager'):
        self.headless = headless
        self.disable_gpu = disable_gpu
        self.page_load_strategy = page_load_strategy

    def config_options(self):
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
            logging.info("Headless enabled")
        if self.disable_gpu:
            chrome_options.add_argument("--disable-gpu")
            logging.info("GPU disabled")
        if self.page_load_strategy:
            chrome_options.page_load_strategy = 'eager'
            logging.info("Page load strategy enabled")
l


