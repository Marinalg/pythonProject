from homework_30.sqlalchemy import VARCHAR, Column, Integer
from ..core.base_model import Base

class Orders(Base):
    __tablename__ = "orders"

    id = Column(VARCHAR(6), primary_key=TRUE)
    order_name = Column(VARCHAR(25))
    customer_name = Column(VARCHAR(25))
    email = Column(VARCHAR(30))
    phone = Column(VARCHAR(30))
    count = Column(Integer)

    def __str__(self)-> str:
        return f"{self.id}|{self.order_name}|{self.customer_name}|{self.email}|{self.phone}|{self.count}"