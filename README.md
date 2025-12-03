# Webscraper Project (BeautifulSoup)

## Structure
```
webscraper_project/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── config/
│   └── settings.py
├── scraper/
│   ├── __init__.py
│   ├── fetcher.py
│   ├── parser.py
│   ├── exporter.py
│   ├── db_mysql.py
│   └── db_mongo.py
├── data/
│   ├── raw_html/
│   └── output.csv
└── sql/
    └── create_table.sql
```

## Quickstart (Local)
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # mac/linux
   venv\Scripts\activate    # windows
   pip install -r requirements.txt
   ```

2. Run the scraper:
   ```bash
   python main.py
   ```

3. Output will be saved to `data/output.csv` and `data/output.json`.

## Multi-page scraping
The scraper follows pagination on `https://quotes.toscrape.com/` and collects quotes, authors and tags across pages.

## Database storage (optional)
### MySQL
- Update `config/settings.py` with your MySQL connection values or set environment variables.
- A sample SQL to create the table is in `sql/create_table.sql`.
- To use MySQL storage, call the `save_to_mysql` function in `scraper/db_mysql.py`.

### MongoDB
- Update `config/settings.py` with MongoDB connection string.
- Use `save_to_mongo` in `scraper/db_mongo.py`.

## Notes
- This project is educational. Respect websites' robots.txt and terms of service.
- Use rate limiting, proper headers and politeness for real scraping tasks.
