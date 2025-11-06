from pkgBackEnd.scraper.course_fetcher import CourseFetcher
from pkgBackEnd.scraper.major_url_fetcher import MajorUrlFetcher
from pkgBackEnd.scraper.semester_url_fetcher import SemesterUrlFetcher
from pkgBackEnd.utils.validators import validate_webdriver, validate_url
import logging

def begin_fetch(driver, base_url):

    validate_webdriver(driver)  #ensures a valid webdriver object has been created.
    validate_url(base_url)      #ensures a valid base url has been obtained.

    semester_url_fetcher = SemesterUrlFetcher(driver, base_url)
    semester_urls: list = semester_url_fetcher.get_semester_urls()
    #semester_urls[0] = fall-2025 semester_urls[1] = summer-2025 semester_urls[2] = spring-2025
    
    if len(semester_urls) < 3:
        logging.error(f"Expected at least 3 semester URLs, but found {len(semester_urls)}. Cannot proceed to fetch major URLs.")
        return

    major_url_fetcher = MajorUrlFetcher(driver, semester_urls[2], base_url)
    major_urls: dict = major_url_fetcher.get_major_urls()

    #creates an object for fetching course data based off major URLs.
    courses = CourseFetcher(driver, major_urls)
    courses.get_courses_data()
