-- full table creation in the database hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table(
       id int, name VARCHAR(256), score INT);

-- inserting rows to the new table
INSERT INTO second_table VALUES(1, 'John', 10);
INSERT INTO second_table VALUES(2, 'Alex', 3);
INSERT INTO second_table VALUES(3, 'Bob', 14);
INSERT INTO second_table VALUES(4, 'George', 8);
