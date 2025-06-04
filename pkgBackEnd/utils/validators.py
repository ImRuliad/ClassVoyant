import logging
from selenium.webdriver.ie.webdriver import WebDriver


def validate_webdriver(webdriver) -> bool:
    if webdriver is not None:
        return True
    else:
        logging.error("webdriver is None.")
        raise

def validate_url(url: str) -> bool:
    if url is not None or url != "":
        return True
    else:
        logging.error("Url is None or empty.")
        raise