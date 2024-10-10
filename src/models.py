from db import get_db

def create_user(name, email, password, role, salary, hire_date, birth_date):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email, password, role, salary, hire_date, birth_date) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (name, email, password, role, salary, hire_date, birth_date))
    db.commit()

def create_department(name, manager):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO departments (name, manager) VALUES (%s, %s)", (name, manager))
    db.commit()

def create_project(name, start_date, end_date, department_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO projects (name, start_date, end_date, department_id) VALUES (%s, %s, %s, %s)",
                   (name, start_date, end_date, department_id))
    db.commit()

def get_all_users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def get_departments():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM departments")
    return cursor.fetchall()

def calculate_average_salary():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT AVG(salary) FROM users")
    return cursor.fetchone()

def count_employees_by_department():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT department_id, COUNT(*) FROM users GROUP BY department_id")
    return cursor.fetchall()

def get_birthdays_this_month():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE MONTH(birth_date) = MONTH(CURRENT_DATE())")
    return cursor.fetchall()
