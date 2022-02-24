from homework_30.sqlalchemy.orm import sessionmaker, Session


driver_name = "postgresql + psycopg2"

host = "localhost"
port = "5432"
database = "mydb"
user = "postgres"
password = "postgres"

engine = create_engine(f"{driver_name}://{user}:{password}@{host}:{port}/{database}")

session_type = sessionmaker(engine)
session: Session = session_type()

