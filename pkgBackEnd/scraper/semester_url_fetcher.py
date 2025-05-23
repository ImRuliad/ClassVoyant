import logging
from pkgBackEnd.utils import validators
from selenium.webdriver.common.by import By


class SemesterUrlFetcher:
    def __init__(self, webdriver, base_url):
        self.webdriver = webdriver
        self.base_url = base_url
        self.list_of_sem_urls = []
        self.semester_link_elements = None
        self.semester_link_element = '[aria-labelledby="article-head"] li a'
        validators.webdriver_exists(self.webdriver)
        validators.url_exists(self.base_url)
        
    def _navigate_to_url(self):
        try:
            self.webdriver.get(self.base_url)
        except Exception as e:
            logging.error(f"Error navigating to base_url: {self.base_url} ---> {e}")
            raise

    def _find_semester_link_elements(self):
        try:
             self.semester_link_elements = self.webdriver.find_elements(By.CSS_SELECTOR, self.semester_link_element)
        except Exception as e:
            logging.error(f"Unable to find semester link element: {self.semester_link_element} ---> {e}")

    def _extract_semester_urls_from_element(self):
        for html_element in self.semester_link_elements:
            semester_url = html_element.get_attribute('href')
            self._add_to_list_of_sem_urls(semester_url)

    def _add_to_list_of_sem_urls(self, semester_url):
        self.list_of_sem_urls.append(semester_url)

    def get_semester_urls(self):
        try:
            self._navigate_to_url()
            self._find_semester_link_elements()
            self._extract_semester_urls_from_element()
            return self.list_of_sem_urls
        except Exception as e:
            logging.error(f"Error getting semester URLs: {e}")
            return
