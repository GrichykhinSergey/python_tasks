class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    color = 'white'

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


school_bus = Bus("School Volvo", 12, 50)
print(type(school_bus))
print(isinstance(school_bus, Vehicle))
