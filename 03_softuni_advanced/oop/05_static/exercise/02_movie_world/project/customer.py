from project.dvd import DVD


class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds: list[DVD] = []

    def __repr__(self):
        formatted_dvds = [p._name for p in self.rented_dvds]
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join(formatted_dvds)})"
