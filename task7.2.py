import random
from random import random
import unittest

n = int(input())
list = []
for i in range(n):
    list.append(round(random(), 2))
print(list)

class TestValue(unittest.TestCase):

    def test_half(self):
        for i in list:
            with self.subTest(i=i):
                self.assertGreaterEqual(i, 0.5)

if __name__ == '__main__':
    unittest.main()