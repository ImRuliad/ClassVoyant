from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import pprint

class CourseFetcher:
    def __init__(self, webdriver, major_urls):
        self.webdriver = webdriver
        self.major_urls: dict = major_urls

    def _set_webdriver_url(self, major_url: str) -> None:
        try:
            self.webdriver.get(major_url)
        except Exception:
            logging.error(f"Unable to set webdriver url for {major_url}")
            raise
    
    def _wait_for_html_element(self):
        WebDriverWait(self.webdriver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.table")))

    def _set_html_element(self):
        html = self.webdriver.page_source            
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def get_courses_data(self):
        course_content = {}
        for major in self.major_urls:
            self._set_webdriver_url(self.major_urls[major])
            self._wait_for_html_element()
            soup = self._set_html_element()
            
            table_divs = soup.select("div.table")
            
            for div in table_divs:
                h2_tag = div.find("h2")
                raw_title = h2_tag.get_text(strip=True)
                course_code, course_title, course_units = (part.strip() for part in raw_title.split('-', 2))
                print(course_code, course_title, course_units)
                
                course_content[course_code] = []
                print(course_code)
        pprint.pprint(course_content)
            

        """
            course_content[course_title] = []

            rows = div.select('div[role="gridcell"]')
            for row in rows:
                print(row.get_text(strip=True))

                course_content[course_title].append(row.get_text(strip=True))
        """
            




