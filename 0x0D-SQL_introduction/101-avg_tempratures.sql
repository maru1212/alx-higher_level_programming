-- Displays the average temperature (Fahrenheit) by the city
-- ordered by tempratur
SELECT city, avg(value) as 'avg_temp'
FROM tempratures
GROUP BY city
ORDER BY avg_temp DESC;
