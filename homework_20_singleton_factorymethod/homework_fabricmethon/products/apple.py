from .product import Product

class Apple(Product):
    def __init__(self) -> None:
        self.__type = "Apple"