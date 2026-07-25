class Item:
    def __init__(self,name,price,quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"{self.name} - ${self.price} (Qty : {self.quantity})"
item1 = Item("Laptop" ,50000,2)
print(item1)