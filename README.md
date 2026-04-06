# 💼 Smart Expense Manager (Real-Time Project)

## 📌 Project Overview

This project is a **Smart Expense Management System** built using **Python and MySQL**.
It helps users to:

* Track daily expenses
* Categorize spending (Food, Travel, Shopping, etc.)
* Analyze where money is being spent
* Generate insights based on spending patterns

This is designed as a **real-time mini project**, simulating how real applications manage financial data.

---

## 🎯 Objective

The main goal of this project is to:

* Store user and expense data in a database
* Perform operations using Python
* Apply functional programming concepts like:

  * `map()`
  * `filter()`
  * `reduce()`
* Use modern Python techniques like:

  * List Comprehension
  * Dictionary Comprehension
* Implement Object-Oriented Programming (OOP)

---

## 🗄️ Database Design (MySQL)

### Users Table

```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);
```

### Expenses Table

```sql
CREATE TABLE expenses (
    exp_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    amount FLOAT,
    category VARCHAR(50),
    description VARCHAR(100),
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

---

## 🐍 Features Implemented

### 🔹 1. User Creation

* Add new users into the system

### 🔹 2. Add Expense

* Add expense details:

  * Amount
  * Category
  * Description
  * Date

---

### 🔹 3. View Expenses

* Display all expenses using **SQL JOIN**

---

### 🔹 4. Filter Expenses

* Filter by:

  * Category
  * Date

✅ Implemented using:

* `filter()`
* List Comprehension

---

### 🔹 5. Total Expense Calculation

* Calculate total expenses

✅ Implemented using:

* `map()`
* `reduce()`

---

### 🔹 6. Category-wise Spending

Example Output:

```
Food: 2000
Travel: 1500
Shopping: 3000
```

✅ Implemented using:

* Dictionary Comprehension

---

### 🔹 7. Update / Delete Expense

* Modify or delete existing expense records

---

## 🧠 OOP Concepts Used

This project follows Object-Oriented Programming principles:

### ✔ Classes

```python
class User:
    pass

class Expense(User):
    pass
```

### ✔ Concepts Covered:

* Encapsulation (private variables)
* Inheritance
* Method Overriding
* super() usage
* Abstract Class

---

## 🔥 Advanced Features

### 📊 1. Monthly Report

* Calculates total spending per month

### 💰 2. Highest Expense

* Finds highest expense using `reduce()`

### 🧠 3. Smart Insight

Example:

```
"You are spending too much on Food this month"
```

---

## 🛠️ Technologies Used

* Python 3.x
* MySQL
* MySQL Connector (Python Library)
* Functional Programming (map, filter, reduce)
* OOP Concepts

---

## ▶️ How to Run the Project

### Step 1: Install Requirements

```bash
pip install mysql-connector-python
```

---

### Step 2: Setup Database

* Open MySQL Workbench
* Run `database.sql` file

---

### Step 3: Update Database Credentials

In `tasks.py`, update:

```python
password="balasb"
```

---

### Step 4: Run Python File

```bash
python tasks.py
```

---

## 📊 Sample Output

```
All Expenses:
[(1, 'Food', 200), (2, 'Travel', 300)]

Filtered Food:
[('Food', 200), ('Food', 1000)]

Total Expense:
1500

Category Wise:
{'Food': 1200, 'Travel': 300}

Monthly Insight:
You are spending too much on Food
```

---

## 📁 Project Structure

```
python-tasks8/
│
├── database.sql
├── tasks.py
├── README.md
```

---

## 🚀 Conclusion

This project demonstrates:

* Real-time expense tracking logic
* Database integration
* Functional programming usage
* Clean OOP design

It can be extended into:

* Web Application
* Mobile App
* Dashboard Analytics System

---

## 🙌 Author

* Developed as part of Python Training Task
* Submitted for evaluation

---

## 🔗 GitHub Repository

(Add your GitHub link here after upload)

```
https://github.com/BalamanikandanSB/python-tasks8
```
