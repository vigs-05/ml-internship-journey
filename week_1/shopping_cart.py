class ShoppingCart:
    def __init__(self):
        self.items = {  }
        self.total_bill = 0
    def add_item(self,item_name,price):
        self.item_name = item_name
        self.price = price
        self.items[item_name] = price
        self.total_bill = self.total_bill + self.price
    def remove_item(self,item_name_remove,price_remove):
        self.item_name_remove = item_name_remove
        self.price_remove = price_remove
        del self.items[item_name_remove]
        self.total_bill = self.total_bill - self.price_remove
    def checkout(self):
        print(self.items)
        print(self.total_bill)
s1 = ShoppingCart()
s1.add_item("Water Bottle" , 20 )
s1.checkout()
s1.add_item("Books" , 200)
s1.checkout()
s1.add_item("Pizza" , 300)
s1.checkout()
s1.remove_item("Water Bottle" , 20)
s1.checkout()
s1.add_item("Phone" , 20000)
s1.checkout()
