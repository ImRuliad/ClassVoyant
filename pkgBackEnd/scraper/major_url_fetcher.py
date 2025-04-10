import logging
import pprint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MajorUrlFetcher:
    def __init__(self, webdriver, semester_urls):
        self.webdriver = webdriver
        self.list_of_semesters = semester_urls

    def _get_divs(self):
        self.webdriver.get(self.list_of_semesters[0])
        wait = WebDriverWait(self.webdriver, 5)
        section_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//section/div")))
        return section_element

    def _get_html_of_divs(self):
        div_element = self._get_divs()

        for element in div_element:
            outer_html = element.get_attribute('outerHTML')
            print(outer_html)

    def get_major_urls(self):
        if not self.webdriver:
            raise ValueError("Webdriver not set!")
        if not self.list_of_semesters:
            raise ValueError("Semester URLs have not been provided")
        self._get_divs()
        self._get_html_of_divs()




