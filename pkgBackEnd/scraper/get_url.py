from pkgBackEnd.FileIO import fileIO


def url():
    return fileIO.url_from_file()

def get_url_content(webdriver):
    webdriver.get(url())
    print(webdriver.page_source)




