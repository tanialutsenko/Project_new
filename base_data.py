import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
import sqlalchemy
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

Base = declarative_base()

class Course(Base):
     __tablename__ = "result_4"

     id = sq.Column(sq.Integer, primary_key=True)
     name = sq.Column(sq.String)
     gender = sq.Column(sq.String)

     def __str__(self):
          return f'{self.id},{self.name} ,{self.gender}'


login = os.getenv('login')
password = os.getenv('password')
database = os.getenv('database')
localhost = os.getenv('localhost')
print(localhost)

DSN = f"postgresql://{login}:{password}@localhost:{localhost}/{database}"

def create_tables():
     engine = sqlalchemy.create_engine(DSN)
     Base.metadata.create_all(engine)

def session():
    engine = sqlalchemy.create_engine(DSN)
    Session = sessionmaker(bind=engine)
    session = Session()

    database_line = []
    for id in session.query(Course).all():
        number = id
        number_1 = str(number)
        data_ingridient = number_1.split(',')
        database_line.append(data_ingridient)
    database = []
    for list in database_line:
        data_user = dict.fromkeys(['id', 'name', 'gender'])
        data_user['id'] = list[0]
        data_user['name'] = list[1]
        data_user['gender'] = list[2]
        database.append(data_user)
    print(database)
    return database



