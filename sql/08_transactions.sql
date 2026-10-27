USE ecom;

SELECT * FROM orders;

SET autocommit = 0;   -- if we set autocommit to 0 its not going to save or auto commit by itself you have to tell manually.
-- And one more thing SET autocommit lasts for the current session only, when you reconnect, it goes back to on.

UPDATE orders 
SET order_status = 'Cancelled'   -- what will happen is, it will update the value to cancelled.
WHERE order_id = 3;

SELECT order_id, customer_name, order_status   -- you can see the change clearly, but its not permanent.
FROM orders;

COMMIT;   -- it will commit the change permanently and it cannot be undone.

-- ROLLBACK;   -- while this will rollback/undo the change.