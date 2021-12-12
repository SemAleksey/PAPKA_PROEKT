from datetime import date


class CarDealership:
    pass


class Car:
    def __init__(self, id: str, model: str, country_of_manufacture: str,
                 date_of_manufacture: date, engine: str, price: str):
        self.id = id
        self.model = model
        self.country_of_manufacture = country_of_manufacture
        self.date_of_manufacture = date_of_manufacture
        self.engine = engine
        self.price = price


class Lorry(Car):
    def __init__(self, id: str, model: str, country_of_manufacture: str,
                 date_of_manufacture: date, engine: str, price: str,
                 maximum_lifting_capacity: str):
        super().__init__(self, id, model, country_of_manufacture,
                         date_of_manufacture, engine, price)
        self.maximum_lifting_capacity = maximum_lifting_capacity
        
        