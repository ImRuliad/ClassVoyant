from pkgBackEnd.configs import get_url_from_env
from pkgBackEnd.scraper.course_fetcher import CourseFetcher
from pkgBackEnd.scraper.major_url_fetcher import MajorUrlFetcher
from pkgBackEnd.scraper.semester_url_fetcher import SemesterUrlFetcher
from pkgBackEnd.utils.validators import validate_webdriver, validate_url


def begin_fetch(driver):
    #obtains base_url from .env file
    base_url = get_url_from_env.base_url()

    #creates object for fetching semester urls. Returns a list of semester URLs.
    #semester_urls[0] = fall-2025 semester_urls[1] = summer-2025 semester_urls[2] = spring-2025
    validate_webdriver(driver)
    validate_url(base_url)

    semester_url_fetcher = SemesterUrlFetcher(driver, base_url)
    semester_urls: list = semester_url_fetcher.get_semester_urls()

    #creates object for fetching major URLs based on their correlated semester URL.
    #returns a dictionary of major URLs.
    #find a way to use validate_url before making the call directly below.
    major_url_fetcher = MajorUrlFetcher(driver, semester_urls[2])
    major_urls: dict = major_url_fetcher.get_major_urls()

    #creates an object for fetching course data based off major URLs.
    courses = CourseFetcher(driver, major_urls)
    courses.get_courses_data()