import unittest
from unittest.mock import patch
from ZiminMykola_HW_20 import MyIterable
from collections.abc import Iterable
from HW_12_ExtendPhonebook import ZiminMykola_HW_12_Task2 as phoneBook

# Task 1

class TestIterable(unittest.TestCase):
    
    def setUp(self):
        self.iter = MyIterable([10, 20, 30, 40, 50])
    
    def test_first_elem(self):
        self.assertEqual(self.iter[0], 10)
        self.assertEqual(self.iter[-1], 50)
        self.assertEqual(self.iter[1:4], [20, 30, 40])
        
    def test_is_iterable(self):
        self.assertIsInstance(self.iter, Iterable)
        self.assertEqual(list(self.iter), [10, 20, 30, 40, 50])
        
        
# Task 2

class TestExtendPhonebook(unittest.TestCase):
    def setUp(self):
        self.test_users = [
            {
                "first_name": "John",
                "last_name": "Peterson",
                "telephone_number": "+1-202-555-0143",
                "city": "Austin",
                "state": "Texas"
            },
            {
                "first_name": "Ann",
                "last_name": "Mitchamm",
                "telephone_number": "+1-305-555-0198",
                "city": "Miami",
                "state": "Florida"
            },
            {
                "first_name": "Theodor",
                "last_name": "Kite",
                "telephone_number": "+1-206-555-0112",
                "city": "Seattle",
                "state": "Washington"
            }
        ]
        
    def test_search_by_first_name(self):
        user = phoneBook.search_by_first_name("Ann", self.test_users)
        self.assertEqual(user, [{
                        "first_name": "Ann",
                        "last_name": "Mitchamm",
                        "telephone_number": "+1-305-555-0198",
                        "city": "Miami",
                        "state": "Florida"
                    }])
        user = phoneBook.search_by_first_name("Adolf", self.test_users)
        self.assertEqual(user, [])
        
    def test_search_by_last_name(self):
        user = phoneBook.search_by_last_name("Kite", self.test_users)
        self.assertEqual(user, [{
                        "first_name": "Theodor",
                        "last_name": "Kite",
                        "telephone_number": "+1-206-555-0112",
                        "city": "Seattle",
                        "state": "Washington"
                    }])
        user = phoneBook.search_by_last_name("Adolf", self.test_users)
        self.assertEqual(user, [])
    
    def test_search_by_full_name(self):
        user = phoneBook.search_by_full_name("Theodor Kite", self.test_users)
        self.assertEqual(user, [{
                                "first_name": "Theodor",
                                "last_name": "Kite",
                                "telephone_number": "+1-206-555-0112",
                                "city": "Seattle",
                                "state": "Washington"
                            }])
        user = phoneBook.search_by_full_name("Adolf", self.test_users)
        self.assertEqual(user, "Please enter both First name and Last name separated by a space.")
        user = phoneBook.search_by_full_name("Adolf Hitler", self.test_users)
        self.assertEqual(user, [])
    
    def test_search_by_telephone_number(self):
        user = phoneBook.search_by_telephone_number("+1-206-555-0112", self.test_users)
        self.assertEqual(user, [{
                                "first_name": "Theodor",
                                "last_name": "Kite",
                                "telephone_number": "+1-206-555-0112",
                                "city": "Seattle",
                                "state": "Washington"
                            }])
        user = phoneBook.search_by_telephone_number("+1-206-515-0111", self.test_users)
        self.assertEqual(user, [])
    
    def test_search_by_city_or_state(self):
        user = phoneBook.search_by_city_or_state("Washington", self.test_users)
        self.assertEqual(user, [{
                                "first_name": "Theodor",
                                "last_name": "Kite",
                                "telephone_number": "+1-206-555-0112",
                                "city": "Seattle",
                                "state": "Washington"
                            }])
        user = phoneBook.search_by_city_or_state("Utah", self.test_users)
        self.assertEqual(user, [])
    
    def test_delete_by_telephone_number(self):
        users_list_len = len(self.test_users)
        result = phoneBook.delete_by_telephone_number("+1-305-555-0198",self.test_users)
        self.assertEqual(result, True)
        self.assertEqual(users_list_len - 1, len(self.test_users))
        
    def test_update_by_telephone_number(self):
        
        self.assertFalse(phoneBook.update_by_telephone_number("+1-555-555-0555", self.test_users))
        
        with patch('builtins.input', side_effect=["Kurt","Cobain","+1-206-555-0333","New York","New York"]):
            result = phoneBook.update_by_telephone_number("+1-206-555-0112", self.test_users)
        self.assertEqual(result, {
                                "first_name": "Kurt",
                                "last_name": "Cobain",
                                "telephone_number": "+1-206-555-0333",
                                "city": "New York",
                                "state": "New York"
                            })



        
if __name__ == '__main__':
    unittest.main()