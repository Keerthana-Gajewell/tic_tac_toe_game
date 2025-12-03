import mysql.connector
from configparser import settings

def save_to_mysql(data):
    cfg = settings.MYSQL
    conn = mysql.connector.connect(
        host=cfg['host'],
        user=cfg['user'],
        password=cfg['password'],
        database=cfg['database'],
        autocommit=True
    )
    cursor = conn.cursor()
    # Ensure table exists - simple schema
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {cfg['table']} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        quote TEXT,
        author VARCHAR(255),
        tags TEXT
    );
    ''')
    insert_sql = f"INSERT INTO {cfg['table']} (quote, author, tags) VALUES (%s, %s, %s)"
    for item in data:
        tags = ",".join(item.get('tags', []))
        cursor.execute(insert_sql, (item.get('quote'), item.get('author'), tags))
    cursor.close()
    conn.close()
    print(f"Saved {len(data)} records to MySQL table {cfg['table']}")
