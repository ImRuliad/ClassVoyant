import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pkgBackEnd.scraper.get_page_content import PageFetcher
from pkgBackEnd.scraper.get_url import UrlFetcher


class WebDriverManager:
    def __init__(self, headless, disable_gpu, page_load_strategy):
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



if __name__ == "__main__":
    manager = WebDriverManager(headless=True, disable_gpu=True, page_load_strategy='normal')
    driver = manager.create_chromedriver()

    url_fetcher = UrlFetcher()
    base_url = url_fetcher.get_base_url()

    page_loader = PageFetcher(driver, base_url)
    page_loader.load_sem_page("fall-2025")
    page_loader.print_page_content("fall-2025")




"""
    url_fetcher = UrlContentFetcher()
    url_fetcher.set_webdriver(driver)
    url_fetcher.get_page_content()
    url_fetcher.print_page_content()
"""







