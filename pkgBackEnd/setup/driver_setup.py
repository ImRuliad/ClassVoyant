import logging
import pprint
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverManager:
    def __init__(self, headless, disable_gpu, page_load_strategy):
        self.driver = None
        self.headless = headless
        self.disable_gpu = disable_gpu
        self.page_load_strategy = page_load_strategy

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
                chrome_options.page_load_strategy = self.page_load_strategy
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

    def quit(self):
        if self.driver:
            self.driver.quit()