import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pkgBackEnd.utils.database_operations import save_course_to_database, save_course_offerings_to_database
import logging

class CourseFetcher:
    def __init__(self, webdriver, major_urls, semester_name):
        self.webdriver = webdriver
        self.major_urls: dict = major_urls
        self.semester_name: str = semester_name

    def _set_webdriver_url(self, major_url: str) -> None:
        try:
            self.webdriver.get(major_url)
        except Exception:
            logging.error(f"Unable to set webdriver url for {major_url}")
            raise
    
    def _wait_for_html_element(self):
        wait_time = 5
        WebDriverWait(self.webdriver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.table")))

    def _set_html_element(self):
        html = self.webdriver.page_source            
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def get_courses_data(self):
        for major in self.major_urls:
            self._set_webdriver_url(self.major_urls[major])
            self._wait_for_html_element()
            soup = self._set_html_element()
            
            table_divs = soup.select("div.table")
            
            for div in table_divs:
                h2_tag = div.find("h2")
                raw_title = h2_tag.get_text(strip=True)
                match = re.match(r'^(.*?) - (.*?) - (\d+ Units)$', raw_title)
                if match:
                    course_code = match.group(1)
                    course_title = match.group(2)
                    course_units = match.group(3)
                    print(course_code, course_title, course_units[0])
                    save_course_to_database(course_code, course_title, int(course_units[0]))
                    save_course_offerings_to_database(course_code, self.semester_name)
                else:
                    logging.error(f"Unable to parse course title: {raw_title}")
                




