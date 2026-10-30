-- Functions in MySQL

-- USE ecom;
-- SELECT * FROM orders;


-- AGGREGATE FUNCTIONS, are those functions that work on multiple rows and return a single value.

-- COUNT

-- SELECT COUNT(*) FROM orders; -- it counts the number of rows a table has.

-- SUM

-- SELECT SUM(quantity * price_per_unit) FROM orders; -- it will multiply the quantity and price_per_unit and then sum all the values.

-- AVERAGE

-- SELECT AVG (price_per_unit) AS average_price FROM orders; -- it will give you the average value in a column name average_price.

-- MIN and MAX

-- SELECT MIN(price_per_unit), MAX(price_per_unit) FROM orders; -- it gives you the minimum value and maximum value


-- SCALAR FUNCTIONS, these work on each row individually.

-- ROUND

-- SELECT customer_name, ROUND(price_per_unit, 0) FROM orders; -- it will roundoff the value or in this case it roundsoff the value to 0 decimal places.

-- UPPER and LOWER

-- SELECT UPPER(customer_name), LOWER(city) FROM orders; -- UPPER will convert the text to uppercase, while LOWER in lowercase.

-- LENGTH

-- SELECT customer_name, LENGTH(customer_name) FROM orders; -- LENGTH prints the length of the string.


-- DATE FUNCTIONS

-- DATE

-- SELECT CURRENT_DATE; -- prints the current date.
-- SELECT CURRENT_TIME; -- prints the current time.

-- DATE DIFF

-- SELECT DATEDIFF(delivery_date,  order_date) FROM orders; -- it gives you the difference between 2 dates.


-- USING FUNCTIONS WITH WHERE

-- SELECT order_date FROM orders WHERE YEAR(order_date) = 2025; -- it will only print the dates which are in year 2025.