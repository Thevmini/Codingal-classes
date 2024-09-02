class Num():
    def __init__(self, no):
        self.no = no

    def __add__(self, other):
        return self.no + other.no
    
    def __sub__(self, other):
        return self.no - other.no

num1 = Num(45)
num2 = Num(23)

print(num1+num2)
print(num1-num2)