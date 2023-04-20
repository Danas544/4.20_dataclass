# Create a dataclass named "Product" that has the following attributes:
#     product_id: int
#     name: str
#     price: float
#     quantity: int
# The class should also have a method named "total_cost" that calculates and returns the total cost of the product, which is the price multiplied by the quantity.
# Create a list of Product objects and write a function that takes this list as input and returns the product with the highest total cost.
# Write a program that creates a list of 5 Product objects, prints out their attributes, and then calls the function to find the product with the highest total cost.

# Klasėje taip pat turėtų būti metodas, pavadintas „total_cost“, kuris apskaičiuoja ir grąžina bendrą produkto kainą, kuri yra kaina, padauginta iš kiekio.
# Sukurkite produkto objektų sąrašą ir parašykite funkciją, kuri šį sąrašą paima kaip įvestį ir grąžina produktą su didžiausia bendra kaina.
# Parašykite programą, kuri sukuria 5 produkto objektų sąrašą, išspausdina jų atributus ir iškviečia funkciją, kad surastų produktą, kurio bendra kaina yra didžiausia.

from dataclasses import dataclass
from collections.abc import Iterator
tes

class Products:
    list_products: list = []

    def get_all_products(self) -> Iterator[str]:
        for product in self.list_products:
            yield f"Name: {product.name}, Price: {product.price}, quantity: {product.quantity}, ID: {product.product_id}"

    def highest_total_cost(self) -> str:
        prices = {}
        for product in self.list_products:
            prices[product.product_id] = product.price * product.quantity

        highest_price_item_id = max(prices, key=lambda x: prices[x])
        product_info = self._get_info_by_id(highest_price_item_id)
        return product_info

    def _get_info_by_id(self, id: int) -> str:
        for product_info in self.list_products:
            if product_info.product_id == id:
                return (
                    f"Name: {product_info.name}, Price: {product_info.price}, quantity: {product_info.quantity},"
                    f" Total price: {product_info.price * product_info.quantity} ID: {product_info.product_id}"
                )
        return f"ERROR 404! not found product by this id: {id}"


@dataclass
class Product(Products):
    product_id: int
    name: str
    price: float
    quantity: int

    def total_cost(self) -> float:
        return self.price * self.quantity

    def add_product(self, Product) -> str:
        Products.list_products.append(Product)
        return f"add this item {Product.name} to item list"


Product1 = Product(product_id=1, name="Agurkas", price=10.00, quantity=5)
print(Product1.total_cost())

Product2 = Product(product_id=2, name="Pomidorai", price=30.00, quantity=10)
Product3 = Product(product_id=3, name="Avokadai", price=50.00, quantity=10)
Product4 = Product(product_id=4, name="Vynuoges", price=5.50, quantity=100)
Product5 = Product(product_id=5, name="Bananai", price=6.99, quantity=250)
print(Product1.add_product(Product1))
print(Product2.add_product(Product2))
print(Product3.add_product(Product3))
print(Product4.add_product(Product4))
print(Product5.add_product(Product5))
list_products = Products()

all_products = list_products.get_all_products()

for product in all_products:
    print(product)

print(list_products.highest_total_cost())
