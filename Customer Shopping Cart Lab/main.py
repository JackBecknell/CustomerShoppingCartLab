from customer import Customer
from product import Product
from shopping_cart import ShoppingCart

karen = Customer()

birthday_cake = Product('A birthday cake.', 40, 'edible')
gallon_of_milk = Product('A gallon of whole milk', 5, 'edible')
plastic_utensils = Product('Plastic utensils', 10, 'non-edible')

#1.
print(karen.name)
#2.
karen.customers_shopping_cart.add_product_to_cart(birthday_cake)
karen.customers_shopping_cart.add_product_to_cart(gallon_of_milk)
karen.customers_shopping_cart.add_product_to_cart(plastic_utensils)
#3.
karen.customer_looks_into_cart()
#4.
karens_total_cost = karen.customers_shopping_cart.total_cost_of_cart()

#5.
karen.customers_shopping_cart.empty_cart()
#6.
karen.customer_looks_into_cart()
