import logging


def webdriver_exists(webdriver) -> None:
    if webdriver is None:
        logging.error("WebDriver is NONE")
        raise ValueError("You must pass a selenium WebDriver instance.")

def url_exists(url: str) -> None:
    if url is None or url == "":
        logging.error("Url is MISSING")
        raise ValueError("You must pass a URL string.")