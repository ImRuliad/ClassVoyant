import logging

from pkgBackEnd.FileIO import fileIO
from bs4 import BeautifulSoup
import requests

def url():
    return fileIO.url_from_file()


def get_url_content():
    try:
        response = requests.get(url())
        response.raise_for_status()
        html_content = response.content
    except requests.exceptions.RequestException as e:
        logging.error(f"Some error occurred while retreiving html content {e}")
    except Exception as e:
        logging.error(f"Some unknown critical error has occurred {e}")
        exit()

    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup.prettify())

if __name__ == "__main__":
    get_url_content()

