### MULTILEVEL INHERITANCE
class Device:
    
    def __init__(self,battery_life):
        self.battery_life = battery_life
    
    def device_info(self):
        print( f"Battery status of Device is {self.battery_life}%" )

class Computer(Device):
    
    def __init__(self,battery_life,ram,cpu):
        super().__init__(battery_life)
        self.ram = ram
        self.cpu = cpu
        
    def computer_info(self):
        print(f"Computer's RAM is {self.ram}GB")
        print(f"Computer's CPU is {self.cpu}")
    
class Laptop(Computer):
    
    def __init__(self,battery_life,ram,cpu,weight):
        super().__init__(battery_life,ram,cpu)
        self.weight = weight
        
    def laptop_info(self):
        print(f"Laptop's Weight is {self.weight}kg")

my_laptop = Laptop(100,32,"i3",1.5)
my_laptop.laptop_info()
my_laptop.computer_info()
my_laptop.device_info()