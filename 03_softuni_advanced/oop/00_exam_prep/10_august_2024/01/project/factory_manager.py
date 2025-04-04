from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:

    PRODUCT_TYPES = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    STORE_TYPES = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.PRODUCT_TYPES:
            raise Exception(f"Invalid product type!")
        product = self.PRODUCT_TYPES[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {'Furniture' if product_type == 'Chair' else 'Toys'} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.STORE_TYPES:
            raise Exception(f"Invalid store type")
        store = self.STORE_TYPES[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            raise Exception(f"Store {store.name} has no capacity for this purchase.")
        valid_products = [p for p in products if p.sub_type in store.store_type()]
        if not valid_products:
            return "Products do not match in type. Nothing sold."
        store.products.extend(valid_products)
        for p in valid_products:
            store.products.append(p)
            store.capacity -= 1
            self.products.remove(p)
            self.income += p.price
        return f"Store {store.name} successfully purchased {len(valid_products)} items."

    def unregister_store(self, store_name: str):
        store_exist = next(
            (store for store in self.stores if store.name == store_name), None
        )
        if store_exist is None:
            raise Exception("No such store!")
        if store_exist.products:
            return "The store is still having products in stock! Unregistering is inadvisable."
        self.stores.remove(store_exist)
        return f"Successfully unregistered store {store_name}, location: {store_exist.location}."

    def discount_products(self, product_model: str):
        products_to_discount = [
            product for product in self.products if product.model == product_model
        ]
        products_count = len(products_to_discount)

        for product in products_to_discount:
            product.discount()

        return (
            f"Discount applied to {products_count} products with model: {product_model}"
        )

    def request_store_stats(self, store_name: str):
        store_exist = next(
            (store for store in self.stores if store.name == store_name), None
        )
        if store_exist is None:
            return "There is no store registered under this name!"
        return store_exist.store_stats()

    def statistics(self):
        product_counts_per_model = {}
        total_price = 0.0
        for product in self.products:
            product.discount()
            product_counts_per_model[product.model] = (
                product_counts_per_model.get(product.model, 0) + 1
            )
            total_price += product.price

        stats = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {total_price:.2f}",
        ]
        for model in sorted(product_counts_per_model.keys()):
            stats.append(f"{model}: {product_counts_per_model[model]}")

        stats.append(f"***Partner Stores: {len(self.stores)}***")
        for store in sorted(self.stores, key=lambda s: s.name):
            stats.append(store.name)

        return "\n".join(stats).strip()
