CREATE DATABASE IF NOT EXISTS alx_book_store;

CREATE TABLE Books(
    book_id VARCHAR(50) PRIMARY KEY, 
    title VARCHAR(130), 
    author_id INT, 
    price DOUBLE, 
    publication_date DATE
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

CREATE TABLE Authors(
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
);