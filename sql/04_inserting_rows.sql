-- CREATE DATABASE e_com;
-- USE e_com;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(150),
    age INT,
    phone VARCHAR(15),
    is_active BOOLEAN,
    signup_date DATE,
    created_at DATETIME,
    total_spent DECIMAL(10,2)
);

-- SELECT * FROM customers;   # For now there is no data, the table is completely empty.

INSERT INTO customers (name, email, age, phone, is_active, signup_date, created_at, total_spent)
VALUES
('Amit Sharma', 'amit@gmail.com', 28, '89898989', TRUE, '2025-01-10', '2025-01-05 10:30:00', 13000.66); 

INSERT INTO customers (name, email, age, phone, is_active, signup_date, created_at, total_spent)
VALUES
('Neha Verma', 'neha@gmail.com', 25, '9123456789', TRUE, '2025-01-12', '2025-01-12 09:15:00', 5400.00),
('Rahul Khan', 'rahul@gmail.com', 32, '9988776655', FALSE, '2025-01-15', '2025-01-15 14:20:00', 0.00);

-- SELECT * FROM customers;   # If you see now the data has been inserted.