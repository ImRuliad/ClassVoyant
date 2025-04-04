import logging

from selenium.webdriver.common.by import By


class SemesterUrlFetcher:
    def __init__(self, webdriver, base_url):
        self.webdriver = webdriver
        self.base_url = base_url
        self.semester_urls = None
        self.list_of_sem_urls = []

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

    def get_semester_urls(self):
        try:
            self._navigate_to_url()
            self.semester_urls = self.webdriver.find_elements(By.CSS_SELECTOR, '[aria-labelledby="article-head"] li a')
            self._save_semester_urls()
            return self.list_of_sem_urls
        except Exception as e:
            logging.error(f"Error getting semester URLs: {e}")
            return

    def _save_semester_urls(self):
        for html_element in self.semester_urls:
            sem_url = html_element.get_attribute('href')
            self.list_of_sem_urls.append(sem_url)




