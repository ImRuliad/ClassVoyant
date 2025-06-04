import logging

from selenium.webdriver.chrome.webdriver import WebDriver
from pkgBackEnd.utils import validators
from selenium.webdriver.common.by import By


class SemesterUrlFetcher:
    def __init__(self, webdriver, base_url):
        self._webdriver: WebDriver = webdriver
        self._base_url: str = base_url
        self._sem_urls: list = []
        self._sem_link_element: str = '[aria-labelledby="article-head"] li a'
        self._semester_link_elements = None
        if not validators.webdriver_exists(self._webdriver):
            logging.error(f"Webdriver does not exist in SemesterUrlFetcher class")
        if not validators.url_exists(self._base_url):
            logging.error(f"Base URL does not exist in SemesterUrlFetcher class")

        
    def _navigate_to_url(self):
        try:
            self._webdriver.get(self._base_url)
        except Exception as e:
            logging.error(f"Error navigating to base_url: {self._base_url} ---> {e}")
            raise

    def _find_semester_link_elements(self):
        try:
             self._semester_link_elements = self._webdriver.find_elements(By.CSS_SELECTOR, self._sem_link_element)
        except Exception as e:
            logging.error(f"Unable to find semester link element: {self._sem_link_element} ---> {e}")

    def _extract_semester_urls_from_element(self):
        for html_element in self._semester_link_elements:
            semester_url = html_element.get_attribute('href')
            self._add_to_list_of_sem_urls(semester_url)

    def _add_to_list_of_sem_urls(self, semester_url):
        self._sem_urls.append(semester_url)

    def get_semester_urls(self):
        try:
            self._navigate_to_url()
            self._find_semester_link_elements()
            self._extract_semester_urls_from_element()
            return self._sem_urls
        except Exception as e:
            logging.error(f"Error getting semester URLs: {e}")
            return
