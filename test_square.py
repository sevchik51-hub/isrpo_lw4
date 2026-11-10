import unittest
from square import *


class Square_Tests(unittest.TestCase):
    def test_baza_area(self):
        result = area(15)
        self.assertEqual(result, 225)

    def test_baza_perimeter(self):
        result = perimeter(5)
        self.assertEqual(result, 20)

    def test_zero_area(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_zero_perimeter(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_big_data_area(self):
        result = area(6823764238764287)
        self.assertEqual(result, 46563758386238349240920746618369)

    def test_big_data_perimeter(self):
        result = perimeter(46735768543368768745368735)
        self.assertEqual(result, 186943074173475074981474940)

    def test_minus_area(self):
        result = area(-5)
        self.assertIsNone(result, "Функция считает некорректные входные двнные!")

    def test_minus_perimeter(self):
        result = perimeter(-12)
        self.assertIsNone(result, "Функция считает некорректные входные двнные!")

    
# для запуска тестов:
# python3 -m unittest test_square.py