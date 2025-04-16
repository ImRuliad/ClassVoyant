import logging
import pprint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class MajorUrlFetcher:
    def __init__(self, webdriver, semester):
        self.semester = semester
        self.dict_of_major_urls = {}
        self.list_of_div_htmls = []
        self.webdriver = webdriver
        self.html_string = None
        self._if_webdriver_sem_url_exists()

    def _if_webdriver_sem_url_exists(self):
        if not self.webdriver:
            logging.error("Web driver not set")
            raise ValueError("Web driver must be passed as an argument when instantiating MajorUrlFetcher")
        if not self.semester:
            logging.error("Semester Url not set")
            raise ValueError("Semester Urls from SemesterUrlFetcher must be passed as an argument when instantiating MajorUrlFetcher")

    def _get_divs(self):
        self.webdriver.get(self.semester)
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
            major_name = item.text.strip()
            major_url = item.get('href')
            self._add_to_dict_major_urls(major_name, major_url)

    def _add_to_dict_major_urls(self, major_name, major_url):
        self.dict_of_major_urls[major_name] = major_url

    def get_major_urls(self):
        if not self.webdriver:
            raise ValueError("Webdriver not set!")
        if not self.semester:
            raise ValueError("Semester has not been provided")
        self._get_divs()
        self._get_html_of_divs()
        self._combine_html_to_string()
        self._extract_href_from_div_html()
        return self.dict_of_major_urls






