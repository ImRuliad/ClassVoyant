from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Courses import Course
import pprint as pp

class CourseFetcher:
    def __init__(self, webdriver, major_urls):
        self.webdriver = webdriver
        self.major_urls: dict = major_urls
        #self.list_of_courses = []

    def _set_webdriver_url(self, major_url: str) -> None:
        try:
            self.webdriver.get(major_url)
        except Exception as e:
            logging.error(f"Unable to set webdriver url for {major_url}")
            raise
    
    def _wait_for_html_element(self):
        WebDriverWait(self.webdriver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.table")))

    def _set_html_element(self):
        html = self.webdriver.page_source            
        soup = BeautifulSoup(html, "html.parser")
        return soup

    #def h2_element_to_course(major_name, course_name):
    #    pass




    def get_courses_data(self):
        #for testing purposes...
        
        self._set_webdriver_url(self.major_urls['Economics'])
        self._wait_for_html_element()
        soup = self._set_html_element()
        table_divs = soup.select("div.table")
        for div in table_divs:
            h2_tag = div.find("h2")
            
            pp.pprint(h2_tag.get_text(strip=True))
    
    """
    FOR TESTING PURPOSES
    """
    def test_get_courses_data(self):
        #for testing purposes...
        for major_name, major_url in self.major_urls.items():

            self._set_webdriver_url(major_url)
            self._wait_for_html_element()
            soup = self._set_html_element()

            table_divs = soup.select("div.table")


            for div in table_divs:
                h2_tag = div.find("h2")
                pp.pprint(h2_tag.get_text(strip=True))
