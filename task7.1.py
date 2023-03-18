import unittest
import random

a = 9.74784
b = 3
string = str(1234567)
list = [2, 3, 4, 1, 6, 8, 2]
listp = list

class TestTests(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(roundn(a), round(a, 2))

    def test_true_or_false(self):
        self.assertTrue(subtract(a,b) <= a)
        self.assertFalse(subtract(a,b) > a)

    def test_in(self):
        self.assertIn(str(b), string)
        self.assertNotIn('8', string)

    def test_compare(self):
        self.assertGreater(addition(a, b), a)
        self.assertLess(b, addition(a, b))

    def test_number_elem(self):
        self.assertCountEqual(shuffling(list), listp)

def roundn(a):
    b = round(a, 2)
    return b

def subtract(a, b):
    c = a - b
    return c

def addition(a, b):
    c = a + b
    return c

def shuffling(list):
    random.shuffle(list)
    return list

if __name__ == '__main__':
    unittest.main()