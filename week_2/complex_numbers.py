class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self,other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return Complex(real_sum,imaginary_sum)
        if real_sum >= 0 and imaginary_sum >= 0:
                return f"Addition is {real_sum}+{imaginary_sum}i"
        elif real_sum >= 0 and imaginary_sum <= 0:
            return f"Addition is {real_sum}{imaginary_sum}i"
        elif real_sum <= 0 and imaginary_sum >= 0:
            return f"Addition is {real_sum}+{imaginary_sum}i"
        else:
            return f"Addition is {real_sum}{imaginary_sum}i"
        
c1 = Complex(1,2)
c2 = Complex(3,4)
c3 = c1 + c2
print(c3)
