from datetime import date


class Shop:
    pass


class Product:
    def __init__(self, id: str, title: str, price: float, count: int):
        self.id = id
        self.title = title
        self.price = price
        self.count = count


class FruitProduct(Product):
    def __init__(self, id: str, title: str, price: float, count: int,
                 country_of_manufacture: str, best_before_date: date ):
        super().__init__(self, id, title, price, count)
        self.country_of_manufacture = country_of_manufacture
        self.best_before_date = best_before_date