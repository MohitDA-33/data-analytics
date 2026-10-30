-- Logical Operators in MySQL, is used to filter data based off conditions.

USE ecom;
SELECT * FROM orders;


-- IN

SELECT * FROM orders WHERE city IN ('Delhi', 'Bangalore', 'Hyderabad'); -- this will only print the rows that have these city.
SELECT * FROM orders WHERE category IN ('Electronics', 'Appliances', 'Kitchen');

-- NOT IN

SELECT * FROM orders WHERE city NOT IN ('Delhi', 'Bangalore', 'Hyderabad'); -- it will print those rows which doesn't match the conditon, output is opposite of IN.
SELECT * FROM orders WHERE payment_mode NOT IN ('UPI', 'Cash');


-- BETWEEN

SELECT * FROM orders WHERE price_per_unit BETWEEN 1000 AND 10000; -- it will print the rows that matches the conditon of having price_per_unit between 1000 to 10000.

-- NOT BETWEEN

SELECT * FROM orders WHERE price_per_unit NOT BETWEEN 1000 AND 10000; -- this will give the opposite output of BETWEEN.


-- WILDCARDS, are used for pattern matching, we use LIKE to use wildcards.

-- % wildcard

SELECT * FROM orders WHERE city LIKE '%i'; -- %i will return the city name that ends with i.
SELECT * FROM orders WHERE city LIKE 'D%';

-- _ wildcard, matches exactly one character.

SELECT * FROM orders WHERE customer_name LIKE 'Sar_ _li'; -- it will only return sara ali cause it matches the pattern.
SELECT * FROM orders WHERE city LIKE "D_lhi";


-- Combining logical conditions

SELECT * FROM orders WHERE category IN ('Electronics', 'Furniture') AND price_per_unit BETWEEN 1000 AND 20000; -- it will first see the condition category and then inside category it will match which are under the price point.