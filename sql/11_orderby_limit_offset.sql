-- ORDER BY, LIMIT, OFFSET in MySQL.

-- ORDER BY, is used to sort data in MySQL. by default it's in ascending order ASC, for descending it's DESC.
-- LIMIT, prints the number of rows that you have defined, example ahead.
-- OFFSET, is used to skip the number of rows you define, again example ahead. 

USE ecom;

SELECT * FROM orders;

-- ORDER BY

SELECT * FROM orders ORDER BY price_per_unit; -- it will sort the data by the column in ascending order (default).
SELECT * FROM orders ORDER BY price_per_unit DESC; -- if you want in descending order.

SELECT * FROM orders ORDER BY city, price_per_unit DESC; -- it will sort the data by two columns first city and then price_per_unit.

-- LIMIT

SELECT * FROM orders LIMIT 5; -- it will print the first 5 rows. 

-- OFFSET, NOTE: you will use OFFSET for pagination.

SELECT * FROM orders LIMIT 5 OFFSET 5; -- it will skip the first 5 and then prints the next 5, 1-5 are skipped and 6-10 are printed.