from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Declarative base from SQLAlchemy
Base = declarative_base()

# Database connection specifics for local Docker SQL Edge Database
server = "db"
user = "dummy_user"
password = "dummy_password"
database = "dummy_db"
conn_string = f"postgresql+psycopg2://{user}:{password}@{server}/{database}"
print(conn_string)

# Create engine
engine = create_engine(conn_string)

# Initialise session class
Session = sessionmaker()

# all_tables = engine.execute(
#     """
#              SELECT
#                  table_schema || '.' || table_name
#              FROM
#                  information_schema.tables
#              WHERE
#                  table_type = 'BASE TABLE'
#              AND
#                  table_schema NOT IN ('pg_catalog', 'information_schema');
#              """
# ).fetchall()
#
# print(len(all_tables))
# table_names = [tables_info[0] for tables_info in all_tables]
# print(table_names)
