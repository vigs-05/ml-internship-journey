class Car:
    wheels = 4 # class properties
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def describe(self):
        print("This a",self.color,self.brand,"with",self.wheels,"wheels")
car1 = Car("Toyota","Red")
car2 = Car("Honda","Blue")        
car1.describe()
car2.describe()