from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

Base = declarative_base()
fake = Faker('ru_RU')

class Client(Base):
    __tablename__ = 'client'

    client_id = Column(Integer, primary_key=True) 
    name_client = Column(String)
    phone_client = Column(String) 
    email_client = Column(String)
    date_of_birth = Column(Date)

DB_USERNAME = 'postgres'
DB_PASSWORD = '111'
DB_HOST = 'localhost'
DB_PORT = '5432' 
DB_NAME = 'dodo_mephi'

connection_string = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(connection_string)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

phone_prefixes = [
    '+7926', '+7904', '+7912', '+7991', 
    '+7937', '+7932', '+7992', '+7495', 
    '+7915', '+7985', '+7986', '+7922', '+7995'
]

for _ in range(300000):  
    name = fake.first_name() 
    phone_prefix = random.choice(phone_prefixes)
    phoneclient = phone_prefix + ''.join(random.choices('0123456789', k=7)) 
    email_domain = random.choice(['@mail.ru', '@gmail.com', '@yandex.ru', '@vk.com', '@inbox.ru'])  
    email = fake.unique.user_name() + email_domain  
    dateofbirth = fake.date_of_birth(minimum_age=14, maximum_age=70) 

    existing_client = session.query(Client).filter( 
        (Client.phone_client == phoneclient) | 
        (Client.email_client == email)
    ).first()

    if existing_client is None:
        client = Client(name_client=name, phone_client=phoneclient, email_client=email, date_of_birth=dateofbirth)

        session.add(client)


try:
    session.commit() 
    print("Данные успешно добавлены в базу данных.")
except Exception as e:
    session.rollback()
    print(f"Произошла ошибка: {e}")
finally:
    session.close()