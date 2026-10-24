-- Updating data in a table

USE ecommerce;

UPDATE orders
SET order_status = 'Delivered'
WHERE order_id = 10;

UPDATE orders
SET delivery_date = '2025-03-05',
    rating = 4
WHERE order_id = 10;

-- SET SQL_SAFE_UPDATES = 0;   -- not recommended at all.

UPDATE orders
SET discount_percent = 10
WHERE customer_name = 'Neha Verma';  -- it will throw an error cause Primary key is missing in the customer name, and sql is in safe update mode.
-- but remember if the safe update is disabled every Neha Verma will be updated in the database;

SELECT * FROM orders;