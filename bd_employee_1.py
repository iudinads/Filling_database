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

phone_prefixes = [
    '+7926', '+7904', '+7912', '+7991', 
    '+7937', '+7932', '+7992', '+7495', 
    '+7915'
]
positions = ['Пицайоло', 'Шеф-повар', 'Повар','Уборщик', 'Менеджер', 'Официант']

num_records = 30500

for _ in range(num_records):
    employee_fullname = fake.name()
    while True:
        phone_prefix = random.choice(phone_prefixes)
        phone_employee = phone_prefix + ''.join(random.choices('0123456789', k=7))

        cur.execute("SELECT COUNT(*) FROM employee WHERE phone_employee = %s;", (phone_employee,))
        if cur.fetchone()[0] == 0:
            break 
    position = fake.random.choice(positions)

    insert_query = """
    INSERT INTO employee (employee_fullname, phone_employee, position)
    VALUES (%s, %s, %s);
    """

    cur.execute(insert_query, (employee_fullname, phone_employee, position))

conn.commit()
cur.close()
conn.close()

print(f"Добавлено {num_records} записей в таблицу 'пиццерия'.")
