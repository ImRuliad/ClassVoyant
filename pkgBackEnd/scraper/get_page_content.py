import logging
from pprint import pprint




class PageFetcher:
    def __init__(self, webdriver, url):
        self.webdriver = webdriver
        self.url_to_fetch = url

    def load_page(self):
        if not self.webdriver:
            raise ValueError(f"chromedriver not set! create_chromedriver() in setup.py not called or chromedriver not passed as parameter")
        if not self.url_to_fetch:
            raise ValueError(f"Url not set! get base_url() in get_url.py not called or url not pass as parameter")

        try:
            self.webdriver.get(self.url_to_fetch)
            return self.webdriver.page_source
        except Exception as e:
            logging.error(f"Error fetching content from {self.url_to_fetch}: {e}")
            raise







    def print_page_content(self):
        content = self.load_page()
        pprint(content)
