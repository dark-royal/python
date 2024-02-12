import unittest

import python_wahala


class MyTestCase(unittest.TestCase):
    def test_number_collectd_from_user_and_store_them_in_a_collection(self):
        number = 10
        expected = list(range(1, number + 1))
        self.assertEqual(expected, python_wahala.user_input(number))

    def test_set_and_and_the_return_the_sum(self):
        numbers = {2, 3, 4, 5, 6, 7, 8}
        expected = 35
        self.assertEqual(expected, python_wahala.sum_collection(numbers))

    def test_set_and_number_remove_number_present_in_the_set(self):
        numbers = {2, 4, 5, 6, 7, 8, 9, 12, 11, 10}
        number = 5
        self.assertEqual(number, python_wahala.remove_element(number, numbers))

    def test_two_set_and_return_new_set(self):
        number1 = {1, 2, 3, 4, 5}
        number2 = {1, 4, 5, 6, 7, 8}
        expected =

