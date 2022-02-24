from typing import List
from homework_30.sqlalchemy.core.base_repository import BaseRepository
from ..models.orders import  Orders


class UserRepository(BaseRepository):


    def get_all_orders(self)->List[Orders]:
        return self._session.query(Orders).all()

    def add_order(self, data: dict):
        order = Order(**data)
        self._session.add(orders)

    def delete_order_attributes(self, email: str, phone: int):
        self._session.query(Orders).filter(Orders.email == email).delete()
        self._seesion.query(Orders).filter(Orders.phone == phone).delete()


