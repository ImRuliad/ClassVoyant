import logging
import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pkgBackEnd.configs import get_url_from_env
from pkgBackEnd.scraper.major_url_fetcher import MajorUrlFetcher
from pkgBackEnd.scraper.semester_url_fetcher import SemesterUrlFetcher
from pkgBackEnd.scraper.course_fetcher import CourseFetcher


class WebDriverManager:
    def __init__(self, headless, disable_gpu, page_load_strategy):
        self.headless = headless
        self.disable_gpu = disable_gpu
        self.page_load_strategy = page_load_strategy

    #leading underscore signifies a "private" function.
    #creates the configuration for options.
    def _config_options(self):
        try:
            chrome_options = Options()
            if self.headless:
                chrome_options.add_argument("--headless")
                logging.info("Headless enabled")
            if self.disable_gpu:
                chrome_options.add_argument("--disable-gpu")
                logging.info("GPU disabled")
            if self.page_load_strategy:
                chrome_options.page_load_strategy = self.page_load_strategy
                logging.info("Page load strategy enabled")
            return chrome_options
        except Exception as e:
            logging.error(f"Error occurred configuring options... {e}")


    def create_chromedriver(self):
        options = self._config_options()

        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            logging.info(f"Chrome driver created successfully")
            return self.driver
        except Exception as e:
            logging.error(f"Error occurred creating chromedriver... {e}")



def run_setup():
    manager = WebDriverManager(headless=True, disable_gpu=True, page_load_strategy='normal')
    driver = manager.create_chromedriver()
    base_url = get_url_from_env.base_url()

        #semester_urls[0] = fall-2025
        #semester_urls[1] = summer-2025
        #semester_urls[2] = spring-2025
    semester_url_fetcher = SemesterUrlFetcher(driver, base_url)
    semester_urls: list = semester_url_fetcher.get_semester_urls()
    print(semester_urls)

    #major_url_fetcher = MajorUrlFetcher(driver, semester_urls[2])
    #major_urls: dict = major_url_fetcher.get_major_urls()
    #pprint.pprint(major_urls)

    #courses = CourseFetcher(driver, major_urls)
    #courses.get_courses_data()


"""
    url_fetcher = UrlContentFetcher()
    url_fetcher.set_webdriver(driver)
    url_fetcher.get_page_content()
    url_fetcher.print_page_content()
"""







