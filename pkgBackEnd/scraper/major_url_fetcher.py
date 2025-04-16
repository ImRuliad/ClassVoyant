import logging
import pprint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class MajorUrlFetcher:
    def __init__(self, webdriver, semester_urls):
        self.list_of_semesters = semester_urls
        self.list_of_major_urls = []
        self.list_of_div_htmls = []
        self.webdriver = webdriver
        self.html_string = None
        self._if_webdriver_sem_url_exists()

    def _if_webdriver_sem_url_exists(self):
        if not self.webdriver:
            logging.error("Web driver not set")
            raise ValueError("Web driver must be passed as an argument when instantiating MajorUrlFetcher")
        if not self.list_of_semesters:
            logging.error("Semester Urls not set")
            raise ValueError("Semester Urls from SemesterUrlFetcher must be passed as an argument when instantiating MajorUrlFetcher")

    def _get_divs(self):
        self.webdriver.get(self.list_of_semesters[0])
        wait = WebDriverWait(self.webdriver, 5)
        section_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//section/div")))
        return section_element

    def _get_html_of_divs(self):
        div_element = self._get_divs()
        for element in div_element:
            outer_html = element.get_attribute('outerHTML')
            self.list_of_div_htmls.append(outer_html)

    def _combine_html_to_string(self):
        self.html_string = "".join(self.list_of_div_htmls)

    def _extract_href_from_div_html(self):
        soup = BeautifulSoup(self.html_string, 'html.parser')
        for item in soup.find_all("a"):
            major_url = item.get('href')
            self.list_of_major_urls.append(major_url)

    def get_major_urls(self):
        if not self.webdriver:
            raise ValueError("Webdriver not set!")
        if not self.list_of_semesters:
            raise ValueError("Semester URLs have not been provided")
        self._get_divs()
        self._get_html_of_divs()
        self._combine_html_to_string()
        self._extract_href_from_div_html()
        return self.list_of_major_urls






