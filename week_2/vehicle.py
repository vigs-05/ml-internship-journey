class Vehicle:
    def __init__(self,brand,max_speed):
        self.brand = brand
        self.max_speed = max_speed
    def intro(self):
        print(f"I am a {self.brand} and my max speed is {self.max_speed}")
class Car(Vehicle):
    def __init__(self, brand, max_speed,num_doors):
        super().__init__(brand, max_speed)
        self.num_doors = num_doors
    def car_details(self):
        print(f"This car has {self.num_doors} doors")
        self.intro()
my_car = Car("Toyota",200,4)
my_car.car_details()
