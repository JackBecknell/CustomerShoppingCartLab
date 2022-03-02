
from product import Product

class ShoppingCart:
    def __init__(self):
        self.products_in_cart = []

    def total_cost_of_cart(self):
        self.total_cost = 0
        for product in self.products_in_cart:
            self.total_cost += product.price_of_product
        print(f'The total cost is ${self.total_cost}')
        

    def add_product_to_cart(self, product_to_add):
        self.products_in_cart.append(product_to_add)

    def empty_cart(self):
        self.products_in_cart = 0


