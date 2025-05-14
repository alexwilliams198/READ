import pandas as pd
from calculator_app import Calculator

def multiply(a, b):
        return a * b

if __name__ == '__main__':
    result = multiply(364, 97)
    print(f"the result of 364 * 97 is {result}")



calc = Calculator(3, 10)
answer_list = calc.times_table()

print(answer_list)
      
