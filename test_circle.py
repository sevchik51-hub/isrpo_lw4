from circle import *
import unittest

class RectangleTestCase(unittest.TestCase):
    def test_baza_area(self):
        result = area(2)
        self.assertEqual(result, 12.566370614359172)
 
    def test_baza_perimeter(self):
        result = perimeter(10)
        self.assertEqual(result, 62.83185307179586)

    def test_zero_area(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_zero_perimeter(self):
        result = perimeter(0)
        self.assertEqual(result, 0)

    def test_point_area(self):
        result = area(1.5)
        self.assertEqual(result, 7.0685834705770345)

    def test_point_perimeter(self):
        result = perimeter(1.5)
        self.assertEqual(result, 9.42477796076938)

    def test_big_data_area(self):
        result = area(23654726)
        self.assertEqual(result, 1757865798148652.8)

    def test_big_data_perimeter(self):
        result = perimeter(7987938475)
        self.assertEqual(result, 50189697660.77451)

    def test_minus_area(self):
        result = area(-25)
        self.assertIsNone(result, "Функция считает некорректные входные двнные!")

    def test_minus_perimeter(self):
        result = perimeter(-8)
        self.assertIsNone(result, "Функция считает некорректные входные двнные!")

if __name__ == '__main__':
    unittest.main()

# для запуска тестов:
# python3 -m unittest test_circle.py