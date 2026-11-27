
# Introduction to SQL and Relational Databases

## 1. What is SQL?

SQL stands for **Structured Query Language**.

It is a standard programming language used to communicate with relational database management systems (RDBMS).

SQL allows us to:
- Create databases and tables.
- Insert data into tables.
- Retrieve information from databases.
- Update existing records.
- Delete records.
- Manage database structures.
- Control access to data.

### Example

```sql
SELECT * FROM Employees;
```

This query retrieves all columns and records from the Employees table.

---

## 2. What is a Database?

A database is an organized collection of data that allows information to be stored, managed, retrieved, and modified efficiently.

### Real-world example

Consider a food delivery application like Swiggy.

It may maintain information about:

- Customers
- Restaurants
- Food items
- Orders
- Payments
- Delivery partners

All this information can be stored in a database.

### Advantages of Databases

1. Organized data storage.
2. Easy data retrieval.
3. Reduced data duplication.
4. Improved data consistency.
5. Data security.
6. Backup and recovery.
7. Multiple users can access data.

---

## 3. What is a Relational Database?

A relational database is a database that stores information in tables consisting of rows and columns.

Tables can be connected to each other through relationships using keys.

For example, consider two tables.

### Customers Table

| customer_id | name | city |
|---|---|---|
| 1 | Rahul | Chennai |
| 2 | Priya | Bangalore |
| 3 | Amit | Mumbai |

### Orders Table

| order_id | customer_id | amount |
|---|---|---|
| 101 | 1 | 500 |
| 102 | 2 | 750 |
| 103 | 1 | 300 |

Here:

- `customer_id` is the Primary Key in Customers.
- `customer_id` is a Foreign Key in Orders.
- The relationship connects customers with their orders.

A relational database helps maintain relationships between different tables.

---

## 4. Understanding Tables, Rows, and Columns

A relational database organizes information using tables.

Consider the Employees table.

| employee_id | name | age | salary |
|---|---|---|---|
| 1 | Rahul | 25 | 45000 |
| 2 | Priya | 23 | 55000 |
| 3 | Amit | 28 | 65000 |

### Table
A table stores related information.

Example: Employees.

### Row (Record)
A row represents one complete record.

Example:

`1, Rahul, 25, 45000`

### Column (Attribute)
A column represents a particular property of the data.

Examples:
- employee_id
- name
- age
- salary

### Cell
A cell represents a single value at the intersection of a row and column.

Example: Rahul's age is 25.

---

## 5. What is RDBMS?

RDBMS stands for **Relational Database Management System**.

It is software used to create, manage, and interact with relational databases.

Popular RDBMS software:

| RDBMS | Description |
|---|---|
| MySQL | Popular open-source relational database |
| PostgreSQL | Advanced open-source relational database |
| Oracle Database | Enterprise-level relational database |
| Microsoft SQL Server | Microsoft's relational database system |
| SQLite | Lightweight embedded relational database |

### SQL vs RDBMS

| SQL | RDBMS |
|---|---|
| A query language | Database management software |
| Used to communicate with databases | Used to manage databases |
| Contains commands such as SELECT and INSERT | Executes SQL commands |
| Example: SELECT * FROM Employees | Example: MySQL |

---

## 6. Important Database Terminologies

| Term | Meaning |
|---|---|
| Database | Organized collection of data |
| Table | Collection of related records |
| Row | Individual record |
| Column | Attribute of a record |
| Primary Key | Uniquely identifies each record |
| Foreign Key | Connects records between tables |
| Schema | Logical structure of a database |
| Constraint | Rule applied to data |
| Query | Instruction sent to a database |
| NULL | Represents missing or unknown data |

---

## 7. Introduction to SQL Commands

SQL commands are commonly divided into five categories.

### 1. DDL – Data Definition Language

Used to define or modify database structures.

Commands:
- CREATE
- ALTER
- DROP
- TRUNCATE

Example:

```sql
CREATE TABLE Employees (
    employee_id INT,
    name VARCHAR(50)
);
```

### 2. DML – Data Manipulation Language

Used to modify data stored inside tables.

Commands:
- INSERT
- UPDATE
- DELETE

Example:

```sql
INSERT INTO Employees
VALUES (1, 'Rahul');
```

### 3. DQL – Data Query Language

Used to retrieve information from databases.

Command:
- SELECT

Example:

```sql
SELECT * FROM Employees;
```

### 4. DCL – Data Control Language

Used to manage database permissions.

Commands:
- GRANT
- REVOKE

### 5. TCL – Transaction Control Language

Used to manage database transactions.

Commands:
- COMMIT
- ROLLBACK
- SAVEPOINT

---

## 8. Creating Your First Database

```sql
CREATE DATABASE CompanyDB;
```

This creates a database named CompanyDB.

To select the database in MySQL:

```sql
USE CompanyDB;
```

---

## 9. Creating Your First Table

```sql
CREATE TABLE Employees (
    employee_id INT,
    name VARCHAR(50),
    age INT,
    salary DECIMAL(10,2),
    city VARCHAR(50)
);
```

### Explanation

- `CREATE TABLE`: Creates a new table.
- `employee_id`: Employee identification number.
- `INT`: Stores integer values.
- `VARCHAR(50)`: Stores text up to 50 characters.
- `DECIMAL(10,2)`: Stores decimal values with two digits after the decimal point.

---

## 10. Inserting Records

```sql
INSERT INTO Employees
(employee_id, name, age, salary, city)
VALUES
(1, 'Rahul', 25, 45000, 'Chennai'),
(2, 'Priya', 23, 55000, 'Bangalore'),
(3, 'Amit', 28, 65000, 'Mumbai');
```

This inserts three employee records into the Employees table.

---

## 11. Retrieving Records

To retrieve all records:

```sql
SELECT * FROM Employees;
```

To retrieve specific columns:

```sql
SELECT name, salary
FROM Employees;
```

To retrieve employees from Chennai:

```sql
SELECT *
FROM Employees
WHERE city = 'Chennai';
```

---

## 12. SQL vs NoSQL

| SQL Databases | NoSQL Databases |
|---|---|
| Relational database model | Non-relational database models |
| Usually stores data in tables | May store data as documents, key-value pairs, graphs, etc. |
| Structured schemas are common | Flexible schemas are common |
| Supports relationships using keys | Relationships are handled differently depending on the database |
| Example: MySQL | Example: MongoDB |

### When to use SQL?

- Banking systems
- Employee management systems
- Hospital management systems
- Inventory management
- Financial applications

### When to use NoSQL?

- Real-time applications
- Large-scale distributed systems
- Flexible document storage
- Applications with rapidly changing data structures

---

## 13. Advantages of Relational Databases

1. Data consistency.
2. Structured data organization.
3. Relationships between tables.
4. Data integrity through constraints.
5. Transaction support.
6. Powerful querying capabilities.
7. Reduced redundancy through normalization.

---

## 14. Practice Questions

### Conceptual Questions

1. What is SQL?
2. What is a database?
3. What is a relational database?
4. What is an RDBMS?
5. Explain the difference between SQL and RDBMS.
6. What are rows and columns?
7. What is a database schema?
8. What is the difference between SQL and NoSQL?
9. What are the five categories of SQL commands?
10. What is the purpose of a Foreign Key?

### Practical SQL Questions

**Question 1:** Create a database called StudentDB.

**Question 2:** Select StudentDB as your active database.

**Question 3:** Create a Students table with:
- student_id
- name
- age
- course
- city

**Question 4:** Insert five student records.

**Question 5:** Display all students.

**Question 6:** Display only student names and courses.

**Question 7:** Find students who belong to Chennai.

**Question 8:** Find students whose age is greater than 20.

---

## 15. Key Takeaways

- SQL is used to communicate with relational databases.
- A database stores organized information.
- An RDBMS manages relational databases.
- Relational databases organize information using tables.
- Rows represent records.
- Columns represent attributes.
- Primary Keys uniquely identify records.
- Foreign Keys establish relationships between tables.
- SQL commands are classified into DDL, DML, DQL, DCL, and TCL.

**Next Topic:** Information and Data Models.
