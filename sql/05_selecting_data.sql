-- CREATE DATABASE ecommerce;
-- USE ecommerce;

-- CREATE TABLE orders (
--     order_id INT PRIMARY KEY AUTO_INCREMENT,
--     customer_name VARCHAR(100),
--     city VARCHAR(50),
--     product VARCHAR(100),
--     category VARCHAR(50),
--     quantity INT,
--     price_per_unit DECIMAL(10,2),
--     discount_percent INT,
--     order_date DATE,
--     delivery_date DATE,
--     payment_mode VARCHAR(30),
--     order_status VARCHAR(30),
--     rating INT
-- );

-- INSERT INTO orders
-- (customer_name, city, product, category, quantity, price_per_unit, discount_percent, order_date, delivery_date, payment_mode, order_status, rating)
-- VALUES
-- ('Amit Sharma', 'Delhi', 'Laptop', 'Electronics', 1, 65000, 10, '2025-01-05', '2025-01-08', 'Credit Card', 'Delivered', 5),
-- ('Neha Verma', 'Mumbai', 'Headphones', 'Electronics', 2, 2500, 0, '2025-01-10', '2025-01-12', 'UPI', 'Delivered', 4),
-- ('Rahul Khan', 'Delhi', 'Office Chair', 'Furniture', 1, 12000, 15, '2025-01-12', '2025-01-20', 'Debit Card', 'Delivered', 5),
-- ('Priya Singh', 'Bangalore', 'Notebook', 'Stationery', 10, 80, 0, '2025-01-15', '2025-01-16', 'Cash', 'Delivered', 3),
-- ('Arjun Mehta', 'Ahmedabad', 'Smartphone', 'Electronics', 1, 30000, 5, '2025-01-18', NULL, 'UPI', 'Cancelled', NULL),
-- ('Sara Ali', 'Delhi', 'Table Lamp', 'Home Decor', 2, 1500, 20, '2025-01-20', '2025-01-23', 'Credit Card', 'Delivered', 4),
-- ('Rohit Gupta', 'Mumbai', 'Water Bottle', 'Kitchen', 5, 500, 0, '2025-01-22', '2025-01-24', 'Cash', 'Delivered', 2),
-- ('Kavita Joshi', 'Pune', 'Backpack', 'Accessories', 1, 3500, 10, '2025-01-25', '2025-01-29', 'Debit Card', 'Delivered', 5),
-- ('Mohammed Faisal', 'Hyderabad', 'Keyboard', 'Electronics', 1, 1800, 0, '2025-01-28', '2025-02-01', 'UPI', 'Delivered', 4),
-- ('Ananya Roy', 'Kolkata', 'Study Table', 'Furniture', 1, 15000, 25, '2025-02-01', NULL, 'Credit Card', 'Pending', NULL),
-- ('Vikram Patel', 'Surat', 'Mixer Grinder', 'Appliances', 1, 4200, 5, '2025-02-03', '2025-02-06', 'UPI', 'Delivered', 4),
-- ('Pooja Nair', 'Chennai', 'Yoga Mat', 'Fitness', 2, 1200, 0, '2025-02-05', '2025-02-07', 'Cash', 'Delivered', 5);


# SELECTING DATA IN A TABLE

SELECT * FROM orders;   # Print all the rows and columns from orders table.

SELECT customer_name, city, product FROM orders;   # Will print only the selected columns

SELECT * FROM orders WHERE city = 'Delhi';    # Will only print the rows that have city = 'Delhi'
SELECT * FROM orders WHERE price_per_unit > 5000;   # Print the rows which have price_per_unit = 5000.

SELECT customer_name, product, price_per_unit FROM orders WHERE price_per_unit > 5000;   # Prints the selected columns and in that selected columns only that rows that have price_per_unit > 5000.
SELECT customer_name, product, price_per_unit FROM orders WHERE price_per_unit !=  5000;   # Is not equal (!=) example.

SELECT * FROM orders WHERE delivery_date IS NULL;   # Prints only the rows which delivery date is NULL, in sql we write is NULL rather than = NULL.

SELECT * FROM orders WHERE city = 'Delhi' AND order_status = 'Delivered';   # Will only print the rows that have city = 'Delhi' and order_status = 'Delivered'.

SELECT customer_name, order_date, price_per_unit FROM orders ORDER BY order_date ASC;   # Prints the selected columns but the rows are in ascending order by order_date.