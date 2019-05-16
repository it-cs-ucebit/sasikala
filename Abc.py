class Abc:
    def __init__(self, a, b):
     self.a = a
     self.b = b
    def __str__(self):
     return "Abc (%d, %d)" % (self.a, self.b)
    def __add__(self,other):
     return Abc(self.a + other.a, self.b + other.b)
a1 = Abc(2,4)
a2 = Abc(5,-2)
print(a1 + a2)
