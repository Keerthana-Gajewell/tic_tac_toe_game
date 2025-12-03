
import requests 

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; Webscraper/1.0; +https://example.com/bot)"
}

def fetch_page(url):
    response =requests.get(url, headers= HEADERS, timeout =10)
    response.raise_for_status()
    return response.text
