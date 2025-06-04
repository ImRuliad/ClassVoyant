import logging

from selenium.webdriver.ie.webdriver import WebDriver


def webdriver_exists(webdriver) -> WebDriver:
    return webdriver is not None

def url_exists(url: str) -> str:
    return url is not None and url != ""