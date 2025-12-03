import os

def save_raw_html(html, page_number):
    path = f"data/raw_html/page_{page_number}.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
