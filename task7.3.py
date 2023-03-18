import os
import unittest
import shutil

way = 'C:/Users/nadya/OneDrive/newFolder'
def folder():
    os.makedirs(way, exist_ok=True)
    with open(way + 'text.txt', 'w') as f:
        f.write("Я говорю: отчего люди не летают так, как птицы? Знаешь, мне иногда кажется, что я птица. Когда стоишь на горе, так тебя и тянет лететь. Вот так бы разбежалась, подняла руки и полетела. Попробовать нешто теперь?")

class TestTextFile(unittest.TestCase):
    def setUp(self):
        folder()

    def test_not_empty(self):
        self.assertIsNotNone("text.txt")

    def tearDown(self):
        shutil.rmtree(way)

if __name__ == '__main__':
    unittest.main()
