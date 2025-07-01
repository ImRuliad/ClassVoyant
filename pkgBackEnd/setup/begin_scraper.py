from pkgBackEnd.scraper.course_fetcher import CourseFetcher
from pkgBackEnd.scraper.major_url_fetcher import MajorUrlFetcher
from pkgBackEnd.scraper.semester_url_fetcher import SemesterUrlFetcher
from pkgBackEnd.utils.validators import validate_webdriver, validate_url, validate_semesters

def begin_fetch(driver, base_url, semester_name: str):
    validate_webdriver(driver)  #ensures a valid webdriver object has been created.
    validate_url(base_url)      #ensures a valid base url has been obtained.

    semester_url_fetcher: SemesterUrlFetcher = SemesterUrlFetcher(driver, base_url) #obtains semester urls from the base url.
    available_semesters: dict = semester_url_fetcher.get_semester_urls()    #dict of semester names and semester urls.
    validate_semesters(available_semesters, semester_name)  #ensures a valid semester name has been obtained.
    
    target_semester_url: str = available_semesters[semester_name]    #assigns a semester url to this variable.

    major_url_fetcher: MajorUrlFetcher = MajorUrlFetcher(driver, target_semester_url, base_url)  #obtains majors based on target semester url.
    major_urls: dict = major_url_fetcher.get_major_urls()   #obtains urls for each major based on target semester url.

    #creates an object to fetch course data from major urls.
    courses = CourseFetcher(driver, major_urls, semester_name)
    courses.get_courses_data()
