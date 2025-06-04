import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverManager:
    def __init__(self, headless, disable_gpu, page_load_strategy):
        self._driver = None
        self._headless = headless
        self._disable_gpu = disable_gpu
        self._page_load_strategy = page_load_strategy

    def _config_options(self):
        try:
            chrome_options = Options()
            if self._headless:
                chrome_options.add_argument("--headless")

            if self._disable_gpu:
                chrome_options.add_argument("--disable-gpu")

            if self._page_load_strategy:
                chrome_options.page_load_strategy = self._page_load_strategy
            return chrome_options

        except Exception as e:
            logging.error(f"Error occurred configuring options... {e}")

    def create_chromedriver(self):
        options = self._config_options()
        try:
            service = Service(ChromeDriverManager().install())
            self._driver = webdriver.Chrome(service=service, options=options)
            return self._driver
        except Exception as e:
            logging.error(f"Error occurred creating chromedriver... {e}")

    def quit(self):
        if self._driver:
            self._driver.quit()