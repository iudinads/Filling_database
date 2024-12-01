
import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

conn = psycopg2.connect(
    dbname='dodo_mephi',
    user='postgres',
    password='111',
    host='localhost',
    port='5432'
)

cur = conn.cursor()

fake = Faker()

cur.execute("SELECT client_id FROM client;") 
clients = cur.fetchall()

num_carts = 150000

card_prefixes = [
    '2204', '2200', '4212', '4317', 
    '4211', '2202', '5336', '4276', 
    '4584', '2005', '4221', '5333'
]

for _ in range(num_carts):
    client = random.choice(clients)

    today = datetime.today()
    min_expiration_date = today + timedelta(days=5 * 365) 

    expiration_date1 = fake.date_between(start_date=min_expiration_date, end_date=today + timedelta(days=365 * 6))

    expiration_date = expiration_date1.strftime("%m-%y")
    card_prefix = random.choice(card_prefixes)
    card_number = card_prefix + ''.join(random.choices('0123456789', k=11))
    cvc = fake.random_int(min=100, max=999)  

    client_id = client[0]
    cur.execute(
        "INSERT INTO card (client_id, expiration_date, card_number, cvc) VALUES (%s, %s, %s, %s);",
        (client_id, expiration_date, card_number, cvc)
    )

conn.commit()
cur.close()
conn.close()
