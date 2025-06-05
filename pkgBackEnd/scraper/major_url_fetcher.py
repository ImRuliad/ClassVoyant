from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from pkgBackEnd.configs import get_url_from_env


class MajorUrlFetcher:
    def __init__(self, webdriver, semester_url):
        self._webdriver = webdriver
        self._semester_url = semester_url
        self._base_url = get_url_from_env.base_url()
        self._major_urls = {}
        self._div_htmls = []
        self._html_string = None

    def _get_divs(self):
        self._webdriver.get(self._semester_url)
        wait = WebDriverWait(self._webdriver, 5)
        section_element = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//section/div"))
        )
        return section_element

    def _get_html_of_divs(self):
        div_element = self._get_divs()
        for element in div_element:
            outer_html = element.get_attribute("outerHTML")
            self._div_htmls.append(outer_html)

    def _combine_html_to_string(self):
        self._html_string = "".join(self._div_htmls)

    def _extract_href_from_div_html(self):
        soup = BeautifulSoup(self._html_string, "html.parser")
        for item in soup.find_all("a"):
            major_name = item.text.strip()
            major_url = item.get("href")
            full_url = self._join_base_and_major_url(major_url)
            self._add_to_dict_major_urls(major_name, full_url)

    def _join_base_and_major_url(self, major_url):
        return self._base_url + major_url[15:]

    def _add_to_dict_major_urls(self, major_name, full_url):
        self._major_urls[major_name] = full_url

    # Implement error handling for obtaining majors
    def get_major_urls(self):
        self._get_divs()
        self._get_html_of_divs()
        self._combine_html_to_string()
        self._extract_href_from_div_html()
        return self._major_urls
