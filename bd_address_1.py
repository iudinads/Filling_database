import random
from faker import Faker
import psycopg2

fake = Faker('ru_RU')

conn = psycopg2.connect(
    dbname='dodo_mephi',
    user='postgres',
    password='111',
    host='localhost',  
    port='5432'       
)
cursor = conn.cursor()

def generate_pizzeria_addresses(num_pizzerias):
    addresses = []
    for pizzeria_id in range(1, num_pizzerias + 1):
        apartment = None
        house_number = random.randint(1, 100) 
        street = fake.street_name()
        city = fake.city()

        addresses.append((pizzeria_id,apartment,house_number, street, city))
    return addresses

def insert_pizzeria_addresses(addresses):
    for address in addresses:
        pizzeria_id, apartment,house_number, street, city = address
        cursor.execute('''
        INSERT INTO address (pizzeria_id, apartment,house_number, street, city)
        VALUES (%s, %s, %s, %s, %s)
        ''', (pizzeria_id, apartment,house_number, street, city))

def generate_fake_client_addresses(num_records):
    for _ in range(num_records):
        client_id = random.randint(1, 299614) 
        apartment = random.randint(1, 100)
        house_number = random.randint(1, 100)
        street = fake.street_name()
        city = fake.city()

        cursor.execute('''
        INSERT INTO address (client_id, apartment, house_number, street, city)
        VALUES (%s, %s, %s, %s, %s)
        ''', (client_id ,apartment, house_number, street, city))

pizzeria_addresses = generate_pizzeria_addresses(400) 
insert_pizzeria_addresses(pizzeria_addresses)

generate_fake_client_addresses(200000) 

conn.commit()
cursor.close()
conn.close()

print("Фейковые данные успешно сгенерированы и сохранены в базе данных.")
