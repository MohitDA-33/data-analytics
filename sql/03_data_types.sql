USE ecom;

CREATE TABLE costumers (
costumer_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100),
email VARCHAR(150),
age INT,
phone VARCHAR(15),
is_active BOOLEAN,
signup_date DATE,
created_at DATETIME,
total_spent DECIMAL(10, 2))
  
SELECT * from costumers;

-- DROP TABLE costumers;   # drops or delete an exisiting table.

-- ALTER TABLE customers RENAME TO clients;   # it will rename from customers to clients.
