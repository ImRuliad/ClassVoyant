from selenium.webdriver.chrome.webdriver import WebDriver
from pkgBackEnd.setup.driver_setup import WebDriverManager
from pkgBackEnd.setup.begin_scraper import begin_fetch
from dotenv import load_dotenv
import os 


def run_setup():
    load_dotenv()
    base_url = os.getenv('BASE_URL')
    
    manager = WebDriverManager(headless=True, disable_gpu=True, page_load_strategy="normal")
    driver: WebDriver = manager.create_chromedriver()
    try:
        begin_fetch(driver, base_url)
    finally:
        manager.quit()







