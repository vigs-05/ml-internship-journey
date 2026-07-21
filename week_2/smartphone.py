### MULTIPLE INHERITANCE
class Phone:
    
    def __init__(self,sim_card):
        self.sim_card = sim_card
    
    def make_call(self):
        print("Dailing.....")
        
class Camera:
    
    def __init(self,lens_size):
        self.lens_size = lens_size
    
    def take_photo(self):
        print("Click")

class Smartphone(Phone,Camera):
    
    def __init__(self, sim_card,lens_size,os):
        super().__init__(sim_card)
        super().__init__(lens_size)
        self.os = os
        
    def phone_info(self):
        print("OS is", self.os)
        self.take_photo()
        self.make_call()
        
my_phone = Smartphone("Airtel","48mm","APPLE")
my_phone.phone_info()