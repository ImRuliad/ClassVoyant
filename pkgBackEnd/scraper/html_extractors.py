from bs4 import BeautifulSoup

def extract_hrefs_from_semester_link_elements(semester_link_elements) -> dict[str, str]:
    sem_urls = {}
    for html_element in semester_link_elements:
        semester_name = html_element.text.strip()
        semester_url = html_element.get_attribute("href")
        if semester_name and semester_url:
            sem_urls[semester_name] = semester_url
    return sem_urls

def extract_outer_html_from_div_elements(divs) -> list[str]:
    div_htmls = []
    div_element = divs
    for element in div_element:
        outer_html = element.get_attribute("outerHTML")
        div_htmls.append(outer_html)
    return div_htmls

def join_div_html_into_string(div_htmls):
    html_string = "".join(div_htmls)
    return html_string

def parse_major_links_from_html(html_string, base_url):
    major_urls = {}
    soup = BeautifulSoup(html_string, "html.parser")
    for item in soup.find_all("a"):
        major_name = item.text.strip()
        major = item.get("href")
        major_url = base_url + major[15:]
        major_urls[major_name] = major_url
    return major_urls
