from pkgBackEnd.configs import get_url_from_env
from pkgBackEnd.scraper.course_fetcher import CourseFetcher
from pkgBackEnd.scraper.major_url_fetcher import MajorUrlFetcher
from pkgBackEnd.scraper.semester_url_fetcher import SemesterUrlFetcher


def begin_fetch(driver):
    base_url = get_url_from_env.base_url()

    semester_url_fetcher = SemesterUrlFetcher(driver, base_url)
    semester_urls: list = semester_url_fetcher.get_semester_urls()

    # semester_urls[0] = fall-2025 semester_urls[1] = summer-2025 semester_urls[2] = spring-2025
    major_url_fetcher = MajorUrlFetcher(driver, semester_urls[2])
    major_urls: dict = major_url_fetcher.get_major_urls()

    courses = CourseFetcher(driver, major_urls)
    courses.get_courses_data()