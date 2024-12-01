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
    product_count = random.choice([0, 1, 2, 3]) 
    product_ids = [random.randint(1, 16) for _ in range(product_count)]

    if product_ids:
        for product_id in product_ids:
            cur.execute("""
                INSERT INTO order_product (order_id, product_id)
                VALUES (%s, %s);
            """, (order_id, product_id))
    else:
        cur.execute("""
            INSERT INTO order_product (order_id, product_id)
            VALUES (%s, NULL);
        """, (order_id,))

conn.commit()
cur.close()
conn.close()
