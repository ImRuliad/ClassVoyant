from pkgBackEnd.scraper.course_fetcher import CourseFetcher
from pkgBackEnd.scraper.major_url_fetcher import MajorUrlFetcher
from pkgBackEnd.scraper.semester_url_fetcher import SemesterUrlFetcher
from pkgBackEnd.utils.validators import validate_webdriver, validate_url
import logging

def begin_fetch(driver, base_url, semester_name: str):

    validate_webdriver(driver)  #ensures a valid webdriver object has been created.
    validate_url(base_url)      #ensures a valid base url has been obtained.

    semester_url_fetcher = SemesterUrlFetcher(driver, base_url) #obtains semester urls from the base url.
    available_semesters: dict = semester_url_fetcher.get_semester_urls()    #dict of semester names and semester urls.
    if not available_semesters:
        logging.error("No available semesters found.")
        return
    if semester_name not in available_semesters:
        logging.error(f"Target semester {semester_name} not found.")
        logging.info(f"Available semesters: {available_semesters}")
        return
    
    target_semester_url = available_semesters[semester_name]    #assigns a semester url to this variable.

    major_url_fetcher = MajorUrlFetcher(driver, target_semester_url, base_url)  #obtains majors based on target semester url.
    major_urls: dict = major_url_fetcher.get_major_urls()   #obtains urls for each major based on target semester url.

    #creates an object to fetch course data from major urls.
    courses = CourseFetcher(driver, major_urls, semester_name)
    courses.get_courses_data()
