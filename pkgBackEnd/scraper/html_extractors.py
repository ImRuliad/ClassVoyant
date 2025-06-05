



def extract_semester_urls_from_element(semester_link_elements):
    sem_urls = []
    for html_element in semester_link_elements:
        semester_url = html_element.get_attribute("href")
        sem_urls.append(semester_url)
    return sem_urls