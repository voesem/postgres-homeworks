-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name text NOT NULL,
	last_name text NOT NULL,
	title text NOT NULL,
	birth_date date NOT NULL,
	notes text NOT NULL
);

CREATE TABLE customers
(
	customer_id text PRIMARY KEY,
	company_name text NOT NULL,
	contact_name text NOT NULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id text REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_city text NOT NULL
);
