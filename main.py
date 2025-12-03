import time
from scraper.fetcher import fetch__page
from scraper.parser import parser_quotes_from_page
from scraper.exporter import save_to_csv, save_to_json
from scraper.db_mysql import ssave_to_mysql
from scraper.db_mongo import save_to_mongo
from configparser import settings

def run_scraper(max_pages=None,delay=1.0,save_mysql= False,save_to_mongo= False):
    all_data = []
    page = 1
    while True:
        url = f"{settings.BASE_URL}/page/{page}/"
        print(f"Fetching {url}")
        page_data = parser_quotes_from_page(url)
        if not page_data:
            print("No more data found, stopping.")
            break
        all_data.extend(page_data)
        page +=1
        if max_pages and page >= max_pages:
            break
        time.sleep(delay)
        print(f"Scraped {len(page_data)} items")
        save_to_csv(all_data, settings.OUTPUT_CSV)
        save_to_json(all_data, settings.OUTPUT_JSON)
        if save_mysql:
            ssave_to_mysql(all_data)
            if save_to_mongo:
                save_to_mongo(all_data)

if __name__ == "__main__":
    run_scraper(max_pages= 3, delay=1.0,save_mysql=False,save_to_mongo=False)
