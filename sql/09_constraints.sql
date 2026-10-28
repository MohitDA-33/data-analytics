-- Constraints in MySQL, there are mainly 4 constraints that are used a lot.

-- UNIQUE, we use it when we dont want any duplicates values in our columns, means all the values should be unique.
-- NOT NULL, doesnt let you store NULL value in your column, you cant write NULL as a value.
-- CHECK, checks a condition if it is satisfied then the value is passed.
-- DEFAULT, if you insert a value, the value will be inserted otherwise instead the default value will be inserted. 

USE ecom;

CREATE TABLE employees (
emp_id INT PRIMARY KEY AUTO_INCREMENT,
email VARCHAR(150) UNIQUE,
name VARCHAR(100) NOT NULL);

INSERT INTO employees (email, name)
VALUES ('amit@company.com', 'Amit Sharma');

-- UNIQUE

INSERT INTO employees (email, name)
VALUES ('amit@company.com', 'rohan Sharma');   -- it will throw an error cause an email already exist by 'amit@company.com'.

-- NOT NULL

INSERT INTO employees (email, name)
VALUES ('amita@company.com', NULL);   -- it will throw an error cause you cant write NULL as a value.

-- CHECK

ALTER TABLE employees
ADD COLUMN age INT CHECK (age >= 18);

INSERT INTO employees (email, name, age)
VALUES ('amita@company.com', 'amita', 17);   -- it will throw error cause the condition doesnt match, the age is 17.

-- DEFAULT

ALTER TABLE employees
ADD COLUMN department VARCHAR(50) DEFAULT 'General';

INSERT INTO employees (email, name, age)
VALUES ('mohit@company.com', 'mohit', 23);   -- it will enter the default value cause i have not entered the value by myself.

SELECT * FROM employees;

-- NOTE: Run each constraints one by one, not all together, otherwise it will throw an error.