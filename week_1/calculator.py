class Calculator:
    greeting = "Welcome to perform some Mathematicals Operations"
    
    @staticmethod
    def get_add(a,b):
        result = a + b
        return result
    
    @staticmethod
    def get_sub(a,b):
        result = a - b
        return result
    
    @staticmethod
    def get_mul(a,b):
        result = a * b
        return result
    
    @staticmethod
    def get_div(a,b):
        result = a / b
        return result
    
    @classmethod
    def get_greeting(cls):
        print(cls.greeting)

Calculator.get_greeting()
print(f"ADDITION IS {Calculator.get_add(6,7)}")
print(f"SUBTRACTION IS {Calculator.get_sub(6,7)}")
Calculator.greeting = "Calculator"
Calculator.get_greeting()
print(f"MULTIPLICATION IS {Calculator.get_mul(6,7)}")
print(f"DIVISION IS {Calculator.get_div(20,2)}")
        