-- Creatng MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Granting privileges to the new user
GRANT ALL
ON mysql.*
TO 'user_0d_1'@'localhost';
