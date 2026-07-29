class NormalStudent:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class FastStudent():
    
    __slots__= ['name', 'age']
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
s1 = NormalStudent("Vignesh" , 20)
s2 = FastStudent("Vignesh" , 20)
print("Normal Student hidden dict : ",s1.__dict__) # WORKS GIVE HIDDEN DICT
s2.marks = 90 # error as not dict available for addition
print("Fast Student hidden dict : ",s2.__dict__) # THROWS ERROR