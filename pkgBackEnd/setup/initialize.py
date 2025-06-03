from pkgBackEnd.configs import get_url_from_env
from pkgBackEnd.scraper.major_url_fetcher import MajorUrlFetcher
from pkgBackEnd.scraper.semester_url_fetcher import SemesterUrlFetcher
from pkgBackEnd.scraper.course_fetcher import CourseFetcher
from pkgBackEnd.setup.driver_setup import WebDriverManager
from pkgBackEnd.setup.begin_scraper import begin_fetch

def run_setup():
    manager = WebDriverManager(headless=True, disable_gpu=True, page_load_strategy='normal')
    driver = manager.create_chromedriver()

    try:
        begin_fetch(driver)
    finally:
        manager.quit()










