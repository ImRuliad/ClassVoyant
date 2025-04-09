import logging
import pprint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MajorUrlFetcher:
    def __init__(self, webdriver):
        self.webdriver = webdriver

    def _get_divs(self, semester_url):
        self.webdriver.get(semester_url)
        wait = WebDriverWait(self.webdriver, 5)
        section_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//section/div")))
        return section_element

    def _get_html_of_divs(self, semester_url):
        div_element = self._get_divs(semester_url)

        for element in div_element:
            outer_html = element.get_attribute('outerHTML')
            print(outer_html)


    def get_major_urls(self, semester_url):
        if not self.webdriver:
            raise ValueError("Webdriver not set!")
        if not semester_url:
            raise ValueError("Semester URL not provided")
        self._get_divs(semester_url)
        self._get_html_of_divs(semester_url)




