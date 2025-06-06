from bs4 import BeautifulSoup


def extract_semester_urls_from_element(semester_link_elements) -> list[str]:
    sem_urls = []
    for html_element in semester_link_elements:
        semester_url = html_element.get_attribute("href")
        sem_urls.append(semester_url)
    return sem_urls

def get_html_of_divs(divs) -> list[str]:
    div_htmls = []
    div_element = divs
    for element in div_element:
        outer_html = element.get_attribute("outerHTML")
        div_htmls.append(outer_html)
    return div_htmls

def combine_html_string(div_htmls):
    html_string = "".join(div_htmls)
    return html_string

def extract_href_from_div_html(html_string, base_url):
    major_urls = {}
    soup = BeautifulSoup(html_string, "html.parser")
    for item in soup.find_all("a"):
        major_name = item.text.strip()
        major = item.get("href")
        major_url = base_url + major[15:]
        major_urls[major_name] = major_url
    return major_urls