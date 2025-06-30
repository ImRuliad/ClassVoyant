import logging
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pkgBackEnd.scraper import html_extractors

class SemesterUrlFetcher:
    def __init__(self, webdriver, base_url):
        self._webdriver: WebDriver = webdriver
        self._base_url: str = base_url

    def _navigate_to_url(self):
        try:
            self._webdriver.get(self._base_url)
            print(self._base_url)    #Debug statement
        except Exception as e:
            logging.error(f"Error navigating to base_url: {self._base_url} ---> {e}")
            raise

    def _find_semester_link_elements(self) -> list[WebElement]:
        sem_link_element: str = '[aria-labelledby="article-head"] li a'
        try:
            semester_link_elements = self._webdriver.find_elements(By.CSS_SELECTOR, sem_link_element)
            return semester_link_elements
        except Exception as e:
            logging.error(f"Unable to find semester link element: {sem_link_element} ---> {e}")
            return []

    def get_semester_urls(self) -> list:
        try:
            self._navigate_to_url()
            sem_url_elements = self._find_semester_link_elements()
            print(sem_url_elements)
            sem_urls = html_extractors.extract_hrefs_from_semester_link_elements(sem_url_elements)
            print(sem_urls)
            return sem_urls
        except Exception as e:
            logging.error(f"Error getting semester URLs: {e}")
            return []
