from shopping_cart import ShoppingCart
class Customer:
    def __init__(self):
        self.name = 'Karen'
        self.customers_shopping_cart = ShoppingCart()
    
    def add_product_to_customer_cart(self, product_to_add):
        self.customers_shopping_cart.add_product_to_cart(product_to_add)

    def customer_looks_into_cart(self):
        for item in self.customers_shopping_cart.products_in_cart:
            print(item.name_of_product)
#BELOW IS TEST CODE
    def calculates_total_cart(self):
        for item in self.customers_shopping_cart.