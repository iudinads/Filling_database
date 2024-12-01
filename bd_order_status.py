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

cur.execute("SELECT order_id FROM orders;") 
order_ids = [row[0] for row in cur.fetchall()]

for order_id in order_ids:
    if random.random() < 0.8:
        status_name = 'исполнен'
    else: 
        status_name = 'отменен'

    insert_query = """
        INSERT INTO order_status (order_id, status_name)
        VALUES (%s, %s);
    """

    cur.execute(insert_query, (order_id, status_name))


conn.commit()

cur.close()
conn.close()

print(f'Вставлено {len(order_ids)} записей в таблицу OrderStatus.')
