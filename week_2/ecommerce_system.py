class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"{self.name} - ₹{self.price}"

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    
    def login(self):
        print(f"{self.name} has logged in.")
        
class Customer(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.cart = []
    
    def add_to_cart(self,product_object):
        self.cart.append(product_object)
    
    def checkout(self):
        print("------------Your Cart------------")
        total_bill = 0
        for item in self.cart:
            print(item)
            total_bill = total_bill + item.price
        print(f"Total Bill : ₹{total_bill}")
            
            
class Seller(User):
    
    def __init__(self, name, email):
        super().__init__(name, email)
        self.inventory ={} # key = product name , value = Product
        
    def add_product(self,product_object):
        self.inventory[product_object.name] = product_object
        
seller1 = Seller("Vighnesh Electronics" ,"vignesh@store.com")
seller1.login()

p1 = Product("Laptop" , 500000)
p2 = Product("Mouse" , 500)
seller1.add_product(p1)
seller1.add_product(p2)

cust1 = Customer("Vickyy" , "vickyy@0501email.com")
cust1.login()

cust1.add_to_cart(seller1.inventory["Laptop"])
cust1.add_to_cart(seller1.inventory["Mouse"])

cust1.checkout()
