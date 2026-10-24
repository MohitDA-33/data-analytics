-- DROP and DELETE table

USE ecom;
SELECT * FROM orders;

DELETE FROM orders;   -- deletes all rows but keeps the table structure.

DROP TABLE orders;   -- deletes everything including structure.

DROP TABLE IF EXISTS orders;   -- only deletes if the table exists otherwise it does nothing instead of giving an error.