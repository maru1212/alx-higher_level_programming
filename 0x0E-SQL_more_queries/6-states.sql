-- Creating a new Database called hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Selecting the new database to use
USE hbtn_0d_usa;

-- Creating a table called states
CREATE TABLE IF NOT EXISTS states(
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256) NOT NULL);
