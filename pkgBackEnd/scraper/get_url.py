import logging
import pprint

from pkgBackEnd.FileIO import get_url_from_file

"""
def url():
    return fileIO.url_from_file()

def get_url_content(webdriver):
    webdriver.get(url())
    print(webdriver.page_source)

"""

class UrlContentFetcher:
    def __init__(self):
        self.webdriver = None
        self.url = None

    def set_webdriver(self, webdriver):
        self.webdriver = webdriver

    def get_url(self):
        self.url = fileIO.url_from_file()
        return self.url

    def get_page_content(self):
        if not self.webdriver:
            raise ValueError("chromedriver not set. call create_chromedriver() first")
        if not self.url:
            try:
                self.get_url()
            except Exception as e:
                logging.error(f"Error getting url: {e} check API_ENDPOINT txt file.")
                raise

        try:
            target_url = self.get_url()
            self.webdriver.get(target_url)
            return self.webdriver.page_source
        except Exception as e:
            logging.error(f"Error fetching content from {self.url}: {e}")
            raise

    def print_page_content(self):
        content = self.get_page_content()
        pprint.pprint(content)







