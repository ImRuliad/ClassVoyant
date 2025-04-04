import logging

from selenium.webdriver.common.by import By


class SemesterUrlFetcher:
    def __init__(self, webdriver, base_url):
        self.webdriver = webdriver
        self.base_url = base_url
        self.semester_urls = None
        self.list_of_sem_urls = []
        self.semester_link_element = '[aria-labelledby="article-head"] li a'

    def _navigate_to_url(self):
        if not self.webdriver:
            raise ValueError("Webdriver not set ")
        if not self.base_url:
            raise ValueError("Base URL not set")
        try:
            self.webdriver.get(self.base_url)
        except Exception as e:
            logging.error(f"Error navigating to base_url: {self.base_url} ---> {e}")
            raise

    def _find_semester_link_elements(self):
        try:
            return self.webdriver.find_elements(By.CSS_SELECTOR, self.semester_link_element)
        except Exception as e:
            logging.error(f"Unable to find semester link element: {self.semester_link_element} ---> {e}")


    def get_semester_urls(self):
        try:
            self._navigate_to_url()
            self.semester_urls = self._find_semester_link_elements()
            self._save_semester_urls()
            return self.list_of_sem_urls
        except Exception as e:
            logging.error(f"Error getting semester URLs: {e}")
            return

    def _save_semester_urls(self):
        for html_element in self.semester_urls:
            sem_url = html_element.get_attribute('href')
            self.list_of_sem_urls.append(sem_url)




