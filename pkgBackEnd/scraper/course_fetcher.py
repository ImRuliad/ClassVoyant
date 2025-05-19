from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint as pp

class CourseFetcher:
    def __init__(self, webdriver, major_urls):
        self.webdriver = webdriver
        self.major_urls = major_urls
        self.list_of_courses = []


    def get_courses_data(self):
        print(self.major_urls['Economics'])
        print(self.webdriver.get(self.major_urls['Economics']))
        
        WebDriverWait(self.webdriver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.table")))

        html = self.webdriver.page_source            
        soup = BeautifulSoup(html, "html.parser")

        table_divs = soup.select("div.table")

        for div in table_divs:
            pp.pprint(div.text.strip())
        


