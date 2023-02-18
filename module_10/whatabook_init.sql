--Title: whatabook_init.sql
--Author: Lucas Cheney
--Date: 02/18/2023
--Description: Whatabook initialization script


-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';


-- create new user 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to whatabook db to whatbook_user 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;


-- drop tables if they exist
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS store;


-- create user table 
CREATE TABLE user (
    user_id         INT             NOT NULL        AUTO_INCREMENT,
    first_name      VARCHAR(75)     NOT NULL,
    last_name       VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
);

-- creat book table
CREATE TABLE book (
    book_id     INT             NOT NULL        AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

-- create wishlist table and set foreign keys
CREATE TABLE wishlist (
    wishlist_id     INT     NOT NULL        AUTO_INCREMENT,
    user_id         INT     NOT NULL,
    book_id         INT     NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book 
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)
);

-- create store table
CREATE TABLE store (
    store_id    INT             NOT NULL        AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
); 

-- insert store records
INSERT INTO store(locale)
    VALUES('2609 Aberdeen Dr. Findlay, OH 45840');

-- insert user records 
INSERT INTO user(first_name, last_name) 
    VALUES('Kasey', 'Cheney');

INSERT INTO user(first_name, last_name)
    VALUES('Alexis', 'Cheney');

INSERT INTO user(first_name, last_name)
    VALUES('Rebeka', 'Cheney');

-- insert book records
INSERT INTO book(book_name, author, details)
    VALUES('Dune', 'Frank Herbert', 'Pauls New Home');

INSERT INTO book(book_name, author, details)
    VALUES('Dune: Messiah', 'Frank Herbert', 'Emprorer Paul has babies');

INSERT INTO book(book_name, author, details)
    VALUES('Children of Dune', 'Frank Herbert', 'The worm and the witch');

INSERT INTO book(book_name, author, details)
    VALUES('God Emporer of Dune', 'Frank Herbert', 'A really big wormy boy');

INSERT INTO book(book_name, author, details)
    VALUES("Harry Potter and the Sorceror's Stone", 'J.K. Rowling', "You're a wizard Harry!");

INSERT INTO book(book_name, author)
    VALUES("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling");

INSERT INTO book(book_name, author, details)
    VALUES("Shogun", 'James Clavell', 'European guy visits the east coast');

INSERT INTO book(book_name, author)
    VALUES('Treasure Island', 'Robert Louis Stevenson');

INSERT INTO book(book_name, author)
    VALUES('The Time Machine', 'H.G. Wells');


-- wishlist values


INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Kasey'),
        (SELECT book_id FROM book WHERE book_name = 'The Time Machine')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Alexis'),
        (SELECT book_id FROM book WHERE book_name = 'Treasure Island')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Rebeka'),
        (SELECT book_id FROM book WHERE book_name = 'Shogun')
    );