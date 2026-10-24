-- ALTER TABLE changes a tables structure and not its data.

USE ecom;
SELECT * FROM orders;

ALTER TABLE orders
ADD COLUMN delivery_partner VARCHAR(50);   -- adds a new column in a table.

ALTER TABLE orders
MODIFY price_per_unit decimal(12, 2);   -- modify an existing column.

ALTER TABLE orders
RENAME COLUMN quantity TO amount;   -- renames a column name.

ALTER TABLE orders
DROP COLUMN delivery_partner;   -- remove/drop an existing column.