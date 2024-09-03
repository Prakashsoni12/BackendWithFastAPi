import requests
from bs4 import BeautifulSoup


def scrape_content(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()


        soup = BeautifulSoup(response.content,'html.parser')
        content = ' '.join(soup.stripped_strings)

        return content
    except requests.RequestException as e:
        print(f"Error scraping URL {url}: {e}")
        return None
    