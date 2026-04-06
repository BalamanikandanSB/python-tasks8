import mysql.connector
import functools

# DB connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="balasb",
    database="expense_db"
)

cursor = conn.cursor()


# ---------------- OOP ----------------

class User:
    def __init__(self, name):
        self.__name = name   # encapsulation

    def get_name(self):
        return self.__name


class Expense(User):

    def __init__(self, name):
        super().__init__(name)

    def add_expense(self, user_id, amount, category, desc, date):
        query = "INSERT INTO expenses(user_id, amount, category, description, date) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query, (user_id, amount, category, desc, date))
        conn.commit()


# ---------------- FUNCTIONS ----------------

def add_user(name):
    cursor.execute("INSERT INTO users(name) VALUES (%s)", (name,))
    conn.commit()


def view_expenses(user_id):
    cursor.execute("""
    SELECT users.name, expenses.amount, expenses.category, expenses.date 
    FROM expenses 
    JOIN users ON users.user_id = expenses.user_id
    WHERE users.user_id = %s
    """, (user_id,))
    return cursor.fetchall()


# 🔥 FILTER
def filter_by_category(data, category):
    return list(filter(lambda x: x[2] == category, data))


def filter_by_date(data, date):
    return [x for x in data if str(x[3]) == date]


# 🔥 MAP + REDUCE
def total_expense(data):
    amounts = list(map(lambda x: x[1], data))
    return functools.reduce(lambda a, b: a + b, amounts, 0)


# 🔥 DICTIONARY COMPREHENSION
def category_wise(data):
    categories = list(set([x[2] for x in data]))

    result = {
        cat: sum([x[1] for x in data if x[2] == cat])
        for cat in categories
    }

    return result


# 🔥 HIGHEST EXPENSE
def highest_expense(data):
    return functools.reduce(lambda a, b: a if a[1] > b[1] else b, data)


# 🔥 MONTHLY REPORT
def monthly_report(data):
    report = {}

    for x in data:
        month = str(x[3])[:7]

        if month not in report:
            report[month] = 0

        report[month] += x[1]

    return report


# 🔥 SMART INSIGHT
def smart_insight(data):
    cat_data = category_wise(data)
    max_cat = max(cat_data, key=cat_data.get)

    return f"You are spending too much on {max_cat}"


# ---------------- TEST DATA ----------------

def insert_sample_data():
    add_user("Mani")

    cursor.execute("SELECT user_id FROM users LIMIT 1")
    user_id = cursor.fetchone()[0]

    exp = Expense("Mani")

    exp.add_expense(user_id, 200, "Food", "Lunch", "2026-04-01")
    exp.add_expense(user_id, 500, "Travel", "Bus", "2026-04-02")
    exp.add_expense(user_id, 300, "Food", "Dinner", "2026-04-03")
    exp.add_expense(user_id, 1000, "Shopping", "Shirt", "2026-04-04")


# ---------------- RUN ----------------

if __name__ == "__main__":
    insert_sample_data()

    data = view_expenses(1)

    print("All Expenses:", data)

    print("Filtered Food:", filter_by_category(data, "Food"))

    print("Total:", total_expense(data))

    print("Category Wise:", category_wise(data))

    print("Highest:", highest_expense(data))

    print("Monthly:", monthly_report(data))

    print("Insight:", smart_insight(data))