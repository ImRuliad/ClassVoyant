import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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

    #leading underscore signifies a "private" function.
    #creates the configuration for options.
    def _config_options(self):
        try:
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
            return chrome_options
        except Exception as e:
            logging.error(f"Error occurred configuring options... {e}")




    def create_chromedriver(self):
        options = self._config_options()

        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            logging.info(f"Chrome driver created successfully")
            return self.driver
        except Exception as e:
            logging.error(f"Error occurred creating chromedriver... {e}")



if __name__ == "__main__":
    manager = WebDriverManager(headless=True, disable_gpu=True, page_load_strategy='eager')
    driver = manager.create_chromedriver()

    get_url_content(driver)





