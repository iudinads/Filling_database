import psycopg2
from faker import Faker
import random

fake = Faker('ru_RU')

conn = psycopg2.connect(
    dbname="dodo_mephi",
    user="postgres",
    password="111",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT employee_id FROM employee;")
employer_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT pizzeria_id FROM pizzeria;")
pizzeria_ids = [row[0] for row in cur.fetchall()]

employee_to_pizzeria = {}
for employee_id in employer_ids:
    pizzeria_id = random.choice(pizzeria_ids)
    employee_to_pizzeria[employee_id] = pizzeria_id

num_records = 300500

for employee_id in employer_ids:
    pizzeria_id = employee_to_pizzeria[employee_id]

    insert_query = """
    INSERT INTO pizza_employee (employee_id, pizzeria_id)
    VALUES (%s, %s);
    """

    cur.execute(insert_query, (employee_id, pizzeria_id))

conn.commit()
cur.close()
conn.close()

print(f"Добавлено {len(employer_ids)} записей в таблицу 'PizzaEmployer'.")
