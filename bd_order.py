import random
from datetime import datetime, timedelta
from faker import Faker
import psycopg2

fake = Faker()

conn = psycopg2.connect(
    dbname='dodo_mephi',
    user='postgres',
    password='111',
    host='localhost',  
    port='5432'       
)
cursor = conn.cursor()


def generate_orders(num_orders):
    orders = []
    for _ in range(num_orders):
        client_id = random.randint(1, 299614) 
        pizzeria_id = random.randint(1, 400)  
        date = fake.date_this_year()

        hour = random.randint(8, 22)
        minute = random.choice([0, 30]) if hour < 22 else random.randint(0, 30) 

        order_datetime = datetime.combine(date, datetime.min.time()) + timedelta(hours=hour, minutes=minute)

        execution_datetime = order_datetime + timedelta(minutes=random.randint(10, 120))  # 
        delivery = random.choice([True, False])
        orders.append((client_id, pizzeria_id, order_datetime, execution_datetime, delivery))

    return orders


num_orders_to_generate = 1005000  
orders = generate_orders(num_orders_to_generate)

insert_query = '''
INSERT INTO orders (client_id, pizzeria_id, order_datetime, execution_datetime, delivery)
VALUES (%s, %s, %s, %s, %s)
'''

cursor.executemany(insert_query, orders) 

conn.commit()
cursor.close()
conn.close()

print(f"{num_orders_to_generate} заказов успешно добавлено в таблицу Orders.")
