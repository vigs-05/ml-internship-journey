class Engine:
    
    def __init__(self,horsepower):
        self.horsepower = horsepower
        
    def start(self):
        print(f"Engine roaring with {self.horsepower} HP!!!")
        
class Car:
    def __init__(self,brand,engine_obj):
        self.brand = brand
        self.engine = engine_obj
        
    def drive(self):
        print(f"{self.brand} is moving....")
        self.engine.start()
        
my_engine = Engine(450)

my_car = Car("Ferrari" , my_engine)

my_car.drive()