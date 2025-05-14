import unittest
from docker_calc.calculator_app import Calculator

class TestOperations(unittest.TestCase):

    #the functions must be named test_something
    def test_sum(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.do_sum(),10, 'The sum is wrong(not 10)!')


    #Test the diff, product , quotient
    def test_diff(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.do_subtract(),6, 'The sum is wrong(not 6)!')
        
    def test_product(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.do_product(),16, 'The sum is wrong(not 16)!') 

    def test_division(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.do_divide(),4, 'The sum is wrong(not 4)!')       



if __name__ == '__main__':
    unittest.main()
