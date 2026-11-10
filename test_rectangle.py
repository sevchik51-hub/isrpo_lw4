import unittest
from rectangle import *

class Rectangle_Tests(unittest.TestCase):
   def test_baza_area(self):
      result = area(15, 10)
      self.assertEqual(result, 150)

   def test_zero1_area(self):
      result = area(27, 0)
      self.assertEqual(result, 0)

   def test_zero2_area(self):
      result = area(0, 30)
      self.assertEqual(result, 0)

   def test_zero3_area(self):
      result = area(0, 0)
      self.assertEqual(result, 0)

   def test_big_data_area(self):
      result = area(67067, 52228001)
      self.assertEqual(result, 3502775343067)

   def test_baza_perimeter(self):
      result = perimeter(10, 5)
      self.assertEqual(result, 30)

   def test_bid_data_perimeter(self):
      result = perimeter(8743635283658465, 72364986637489547632895)
      self.assertEqual(result, 144729990762249662582720)

   def test_minus_area(self):
      result = area(-25, 8)
      self.assertIsNone(result, "Функция считает некорректные входные двнные!")

   def test_minus_perimeter(self):
      result = perimeter(-8, -2)
      self.assertIsNone(result, "Функция считает некорректные входные двнные!")

# для запуска тестов:
# python3 -m unittest test_rectangle.py