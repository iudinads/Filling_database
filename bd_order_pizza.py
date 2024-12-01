import psycopg2
from faker import Faker
import random


fake = Faker()

conn = psycopg2.connect(
    dbname='dodo_mephi',
    user='postgres',
    password='111',
    host='localhost',
    port='5432'
)

cur = conn.cursor()

order_ids = range(1, 1005001)

for order_id in order_ids:
    pizza_count = random.choice([0, 1, 2, 3])
    pizza_ids = [random.randint(1, 50) for _ in range(pizza_count)]

    if pizza_ids:
        for pizza_id in pizza_ids:
            cur.execute("""
                INSERT INTO order_pizza (order_id, pizza_id)
                VALUES (%s, %s);
            """, (order_id, pizza_id))
    else:
        cur.execute("""
            INSERT INTO order_pizza (order_id, pizza_id)
            VALUES (%s, NULL);
        """, (order_id,))

conn.commit()
cur.close()
conn.close()
