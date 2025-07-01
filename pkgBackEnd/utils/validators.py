import logging
from selenium.webdriver.ie.webdriver import WebDriver

#make these more verbose.
def validate_webdriver(webdriver) -> bool:
    if webdriver is not None:
        return True
    else:
        logging.error("webdriver is None.")
        raise

#make these more verbose.
def validate_url(url: str) -> bool:
    if url is not None or url != "":
        return True
    else:
        logging.error("Url is None or empty.")
        raise

def validate_semesters(available_semesters: dict, semester_name: str) -> bool:
    if not available_semesters:
        logging.error("No available semesters found.")
        raise
    if semester_name not in available_semesters:
        logging.error(f"Target semester {semester_name} not found.")
        logging.info(f"Available semesters: {available_semesters}")
        raise
    return True