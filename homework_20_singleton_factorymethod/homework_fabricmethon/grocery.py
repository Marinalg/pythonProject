from homework_20_singleton_factorymethod.products.product import Banana
from homework_20_singleton_factorymethod.products.product import Apple
from homework_20_singleton_factorymethod.products.product import Stawberry
from homework_20_singleton_factorymethod.products.product import Product

class GroceryMarket:
    @staticmethod
    def get_product(type: str):

        if type == "banana":
                return Banana()
            if type == "apple":
                    return Apple()
            elif type == "strawberry":
                        return Strawberry()
                else:
                    raise Exception("Not delicious product.")



