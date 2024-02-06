import unittest
import ascending_order

class TestAscendingFunction(unittest.TestCase):
    def test_that_function_is_not_none(self):
        self.assertIsNone(ascending_order.ascending_function)

        ##def test_that_function_sort_array_in_ascending_order(self):
           ## sample_list = [10,2,8,9,3,4,1,5]
           ## sample_output =[1,2,3,4,5,8,9,10]
            ##self.assertEqual(ascending_order.ascending_function(sample_list),sample_output)