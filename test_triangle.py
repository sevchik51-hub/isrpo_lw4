import unittest
from triangle import *

class Triangle_Tests(unittest.TestCase):
   def test_baza_area(self):
      result = area(5, 2)
      self.assertEqual(result, 5)

   def test_baza_perimeter(self):
      result = perimeter(5, 6, 7)
      self.assertEqual(result, 18)

   def test_zero_area1(self):
      result = area(0, 5)
      self.assertEqual(result, 0)

   def test_zero_area2(self):
      result = area(0, 5)
      self.assertEqual(result, 0)

   def test_zero_area3(self):
      result = area(0, 5)
      self.assertEqual(result, 0)

   def test_zero_perimeter(self):
      result = perimeter(0, 0, 0)
      self.assertEqual(result, 0)

   def test_big_data_area(self):
      result = area(6823764238764287, 326748)
      self.assertEqual(result, 1114825658743876624338)

   def test_big_data_perimeter(self):
      result = perimeter(46735768543368768745368735, 287467283, 12364753843695)
      self.assertEqual(result, 46735768543381133786679713)

   def test_minus_area(self):
      result = area(-6, -4)
      self.assertIsNone(result, "Функция считает некорректные входные двнные!")

   def test_minus_perimeter(self):
      result = perimeter(-8, 3, 0)
      self.assertIsNone(result, "Функция считает некорректные входные двнные!")


# для запуска тестов:
# python3 -m unittest test_triangle.py