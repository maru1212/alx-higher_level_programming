-- Creating database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creating a new user called user_0d_2.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Granting privilege of only SELECT for the new user.
GRANT SELECT
ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost';
