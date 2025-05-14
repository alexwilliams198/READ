class Calculator:
    def __init__(self, a, b):
       self.a = a
       self.b = b
    def do_sum(self):
        return self.a + self.b

    def do_product(self):
        return self.a * self.b

    def do_subtract(self):
        return self.a - self.b

    def do_divide(self):
        return self.a / self.b
    
    def times_table(self):
        results = []
        for i in range (1, self.b + 1):
            results.append(
            
            (f"{self.a} x {i} = {self.a * i}")
            )
            return results
#myCalc = Calculator(11,6)
#print(myCalc.do_sum()) 
