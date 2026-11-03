USE ecom;

SELECT *FROM orders;
SELECT *FROM sellers;

-- Here: orders table is a child table. while sellers table is a parent. and seller_id connects them.

ALTER TABLE orders
DROP FOREIGN KEY fk_orders_sellers;


-- CASCADE

ALTER TABLE orders
ADD CONSTRAINT fk_orders_sellers
FOREIGN KEY (seller_id)
REFERENCES sellers(seller_id)
ON DELETE CASCADE;

DELETE FROM sellers
WHERE seller_id = 2; -- seller with seller_id = 2 is deleted. every order linked to that have seller will be deleted.


-- SET NULL

ALTER TABLE orders
MODIFY seller_id INT NULL; -- seller_id in orders must allow null for this to work.

ALTER TABLE orders
ADD CONSTRAINT fk_orders_sellers
FOREIGN KEY (seller_id)
REFERENCES sellers(seller_id)
ON DELETE SET NULL;

DELETE FROM sellers
WHERE seller_id = 1; -- it will remove seller_id from sellers table, but keeps the order by putting null in the place.


-- BY DEFAULT, its RESTRICT

ALTER TABLE orders
ADD CONSTRAINT fk_orders_sellers
FOREIGN KEY (seller_id)
REFERENCES sellers(seller_id);


-- COMPARISION:

-- CASCADE: deletes orders automatically.
-- SET NULL: keeps the orders, but removes the seller link
-- RESTRICT: blocks seller deletion.