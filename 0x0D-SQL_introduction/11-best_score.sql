-- lists all records with score >= 10 in the table second_table
SELECT score, name FROM second_table
       where score >= 10 ORDER BY score DESC;
