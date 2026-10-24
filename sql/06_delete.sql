USE ecom;
SELECT * FROM orders;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM orders
WHERE delivery_date IS NULL;

DELETE FROM orders
WHERE order_id = 2;

DELETE FROM orders;   # this empties the table completely, but keep the structure as it is.