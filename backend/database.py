import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Declarative base from SQLAlchemy
Base = declarative_base()

# Database connection specifics for local Docker SQL Edge Database
server = os.environ["DB_SERVER"]
user = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
database = os.environ["DB_NAME"]
conn_string = f"postgresql+psycopg2://{user}:{password}@{server}/{database}"

print('-----')
print(conn_string)
print('-----')

# Create engine
engine = create_engine(conn_string)

# Initialise session class
Session = sessionmaker()
