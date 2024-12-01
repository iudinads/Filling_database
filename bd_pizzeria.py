import psycopg2
from faker import Faker
import random

fake = Faker()

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

num_records = 750

for _ in range(num_records):
    phone_prefix = random.choice(phone_prefixes)
    phone_pizzeria = phone_prefix + ''.join(random.choices('0123456789', k=7))
    opening_times = ["08:00:00", "09:00:00"]
    closing_times = ["22:00:00", "23:00:00"]

    opening_time = random.choice(opening_times)
    closing_time = random.choice(closing_times)

    while closing_time <= opening_time:
        closing_time = fake.time()

    insert_query = """
    INSERT INTO pizzeria (phone_pizzeria, opening_time, closing_time)
    VALUES (%s, %s, %s);
    """

    cur.execute(insert_query, (phone_pizzeria, opening_time, closing_time))

conn.commit()
cur.close()
conn.close()

print(f"Добавлено {num_records} записей в таблицу 'пиццерия'.")
