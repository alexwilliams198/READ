import unittest
import pandas as pd
from clean_library_data import enrich_dateDuration
from pandas.api.types import is_integer_dtype #add your functions that you want to test

class TestOperations(unittest.TestCase):

    def setUp(self):
        #creating a test dataframe
        self.df = pd.DataFrame({
            'Book checkout': pd.to_datetime(['2023-01-01']),
            'Book Returned': pd.to_datetime(['2023-01-10'])})
        
        self.df = enrich_dateDuration(colA='Book checkout', colB='Book Returned', df=self.df)

    def test_date_delta_is_integer(self):
        self.assertIn('date_delta', self.df.columns, "Missing 'date_delta' column")
        self.assertTrue(
            is_integer_dtype(self.df['date_delta']),
            "The 'date_delta' column is not of integer dtype")

    def test_date_delta_positive(self):
        self.assertTrue(
            (self.df['date_delta'] >= 0).all(),
            "Some values in 'date_delta' are below zero")    


if __name__ == '__main__':
    unittest.main()

   

    
#At a a minimum test these:
#check that the duration column (between checkout and return)is an integer
# check that the same column is above zero
# do any other function you've created (or mine)

#is_integer_dtype