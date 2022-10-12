import requests
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession


def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def get_results(query, start=10):

    response = get_source(
        f"https://www.google.com/search?q={query}&start={start}")

    return response


def parse_results(response):

    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"

    results = response.html.find(css_identifier_result)

    output = []

    for result in results:

        item = {
            'Title': result.find(css_identifier_title, first=True).text,
            'Link': result.find(css_identifier_link, first=True).attrs['href'],
            'Text': result.find(css_identifier_text, first=True).text
        }

        output.append(item)

    return output


def google_search(query):
    response = get_results(query)
    return parse_results(response)


results = google_search("online defensive driving school US")

csvFile = pd.DataFrame(results)
csvFile.to_csv('results.csv', index=False)
