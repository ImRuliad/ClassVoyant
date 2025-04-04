import logging
import pprint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MajorUrlFetcher:
    def __init__(self, webdriver):
        self.webdriver = webdriver

    def get_major_urls(self, semester_url):
        if not self.webdriver:
            raise ValueError("Webdriver not set!")
        if not semester_url:
            raise ValueError("Semester URL not provided")

        self.webdriver.get(semester_url)
        wait = WebDriverWait(self.webdriver, 5)
        section_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//section/div")))

        for div_element in section_element:
            outer_html = div_element.get_attribute('outerHTML')
            print(outer_html)



"""
       try:
            self.webdriver.get(semester_url)
            html_elements = self.webdriver.find_elements(By.TAG_NAME, "div")


            for element in html_elements:
                element_content = element.get_attribute("textContent")
                if element_content:
                    print(element_content)

        except Exception as e:
            logging.error(f"Error extracting major API urls from {semester_url}: {e}")
            raise

"""