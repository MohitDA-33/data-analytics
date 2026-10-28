-- PRIMARY KEY and AUTO INCREMENT

-- PRIMARY KEY - it's basically a unique identifier like a roll number, the value can't be null and cannot be duplicated.
-- AUTO_INCREMENT -  automatically generates next numbers for a column 1, 2, 3, 4.. 

USE ecom; 

-- CREATE TABLE employees (
--     emp_id INT PRIMARY KEY AUTO_INCREMENT,
--     email VARCHAR(150) UNIQUE,
--     name VARCHAR(100) NOT NULL
-- );

-- INSERT INTO employees (email, name)
-- VALUES ('amit@company.com', 'Amit Sharma'); -- i can insert the data without giving emp_id, cause this part will be taken care automatically.

-- ALTER TABLE employees
-- ADD PRIMARY KEY (email); -- it will throw an error cause a table can only have only PRIMARY KEY, and its already assigned to emp_id.

SELECT * FROM employees; -- in the table you can see that the emp_id is added automatically.
