from db import get_db

def seed_data():
    db = get_db()
    cursor = db.cursor()

    # Insertar departamentos
    departments = [("IT", "John Doe"), ("HR", "Jane Smith"), ("Finance", "Mark Johnson")]
    cursor.executemany("INSERT INTO departments (name, manager) VALUES (%s, %s)", departments)

    # Insertar usuarios
    users = [
        ("Alice", "alice@example.com", "Password123", "admin", 50000, "2020-01-15", "1990-02-20"),
        ("Bob", "bob@example.com", "Password123", "user", 45000, "2020-02-15", "1991-03-25"),
        ("Charlie", "charlie@example.com", "Password123", "user", 40000, "2020-03-15", "1992-04-30"),
        ("David", "david@example.com", "Password123", "user", 35000, "2020-04-15", "1993-05-15"),
        ("Eva", "eva@example.com", "Password123", "user", 30000, "2020-05-15", "1994-06-10"),
    ]
    cursor.executemany("INSERT INTO users (name, email, password, role, salary, hire_date, birth_date) VALUES (%s, %s, %s, %s, %s, %s, %s)", users)

    # Insertar proyectos
    projects = [("Project A", "2023-01-01", "2023-06-30", 1), ("Project B", "2023-02-01", "2023-08-30", 2)]
    cursor.executemany("INSERT INTO projects (name, start_date, end_date, department_id) VALUES (%s, %s, %s, %s)", projects)

    db.commit()
    print("Datos de ejemplo insertados.")

if __name__ == '__main__':
    seed_data()
