# from homework_30.sqlalchemy import VARCHAR, create_engine, Column, Integer
# from homework_30.sqlalchemy.orm import declarative_base, sessionmaker, Session
#
#
# driver_name = "postgresql + psycopg2"
#
#
# host = "localhost"
# port = "5432"
# database = "mydb"
# user = "postgres"
# password = "postgres"
#
# engine = create_engine(f"{driver_name}://{user}:{password}@{host}:{port}/{database}")
#
# Base = declarative_base()
#
# class Orders(Base):
#     __tablename__ = "orders"
#
#     id = Column(VARCHAR(6), primary_key=TRUE)
#     order_name = Column(VARCHAR(25))
#     customer_name = Column(VARCHAR(25))
#     email = Column(VARCHAR(30))
#     phone = Column(VARCHAR(30))
#     count = Column(Integer)
#
#     def __str__(self)-> str:
#         return f"{self.id}|{self.order_name}|{self.customer_name}|{self.email}|{self.phone}|{self.count}"
#
# session_type = sessionmaker(engine)
# session: Session = session_type()
#
# for order in orders:
#     print(order)