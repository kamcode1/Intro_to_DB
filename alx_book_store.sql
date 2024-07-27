CREATE DATABASE IF NOT EXISTS alx_book_store;

CREATE TABLE Books(book_id VARCHAR(50) PRIMARY KEY, title VARCHAR(130), author_id INT FOREIGN KEY, price DOUBLE, publication_date DATE)