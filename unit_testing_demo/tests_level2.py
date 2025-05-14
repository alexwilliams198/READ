import unittest
from calculator_app import Calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.calculation=Calculator(8,2)

    #the functions must be named test_something
    def test_sum(self):
        self.assertEqual(self.calculation.do_sum(),10, 'The sum is wrong(not 10)!')

    def test_diff(self):
        self.assertEqual(self.calculation.do_subtract(),6, 'The sum is wrong(not 6)!')
        
    def test_product(self):
        self.assertEqual(self.calculation.do_product(),16, 'The sum is wrong(not 16)!') 

    def test_division(self):
        self.assertEqual(self.calculation.do_divide(),4, 'The sum is wrong(not 4)!')       



if __name__ == '__main__':
    unittest.main()
