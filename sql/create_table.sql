CREATE DATABASE IF NOT EXISTS webscraper_db;
USE webscraper_db;

CREATE TABLE IF NOT EXISTS quotes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quote TEXT,
    author VARCHAR(255),
    tags TEXT
);
