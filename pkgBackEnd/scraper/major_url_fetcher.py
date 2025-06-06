from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from pkgBackEnd.configs import get_url_from_env
from pkgBackEnd.scraper import html_extractors

class MajorUrlFetcher:
    def __init__(self, webdriver, semester_url):
        self._webdriver = webdriver
        self._semester_url = semester_url
        self._base_url = get_url_from_env.base_url()

    def _get_divs(self):
        self._webdriver.get(self._semester_url)
        wait = WebDriverWait(self._webdriver, 5)
        section_element = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//section/div"))
        )
        return section_element


    # Implement error handling for obtaining majors
    def get_major_urls(self):
        divs = self._get_divs()
        div_htmls = html_extractors.get_html_of_divs(divs)
        html_string = html_extractors.combine_html_string(div_htmls)
        major_urls = html_extractors.extract_href_from_div_html(html_string, self._base_url)
        return major_urls

