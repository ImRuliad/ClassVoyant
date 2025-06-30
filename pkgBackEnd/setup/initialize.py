from selenium.webdriver.chrome.webdriver import WebDriver
from pkgBackEnd.setup.driver_setup import WebDriverManager
from pkgBackEnd.setup.begin_scraper import begin_fetch

def run_setup(base_url: str):
    manager = WebDriverManager(headless=True, disable_gpu=True, page_load_strategy="normal")
    driver: WebDriver = manager.create_chromedriver()
    try:
        begin_fetch(driver, base_url)
    finally:
        manager.quit()







