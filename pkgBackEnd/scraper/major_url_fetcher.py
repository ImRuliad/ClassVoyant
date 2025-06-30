from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from pkgBackEnd.scraper import html_extractors


class MajorUrlFetcher:
    def __init__(self, webdriver, semester_url, base_url):
        self._webdriver = webdriver
        self._semester_url = semester_url
        self._base_url = base_url

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
        div_htmls = html_extractors.extract_outer_html_from_div_elements(divs)
        html_string = html_extractors.join_div_html_into_string(div_htmls)
        major_urls = html_extractors.parse_major_links_from_html(html_string, self._base_url)
        return major_urls

