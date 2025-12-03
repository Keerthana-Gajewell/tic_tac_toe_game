from bs4 import BeautifulSoup 

def parse_quote(html):
    soup = BeautifulSoup(html, 'html.paser')
    quotes= []

    for q in soup.Select('div.quote'):
        text_tag = q.select_one('span.text')
        author_tag = q.select('small.author')
        tags = [t.get_text(strip = True) for t in q.select("div.tags a.tags")]
        if text_tag and author_tag:
            quotes.append({
            "quote": text_tag.get_text(strip= True),
            "author": author_tag.get_text(strip= True),
            "tags": tags
            })
            return quotes