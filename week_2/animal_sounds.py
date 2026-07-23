class Animal:
    def __init__(self,name):
        self.name = name
        
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def make_sound(self):
        print(f'{self.name} says Bark!!!')
        
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print(f'{self.name} says Meow!!!')
        
my_animals = [Dog("Sheru"),Cat("Whiskers"),Animal("Unknown")]
for animal in my_animals:
    animal.make_sound()