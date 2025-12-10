import unittest
import math
import rectangle
import square
import triangle
import circle

class RectangleTestCase(unittest.TestCase):
    # area
    def test_zero_area(self):
       res = rectangle.area(10, 0)
       self.assertEqual(res, 0)
    def test_square_area(self):
       res = rectangle.area(10, 10)
       self.assertEqual(res, 100)
    def test_normal_area(self):
       res = rectangle.area(5, 7)
       self.assertEqual(res, 35)
    def test_normal_float_area(self):
       res = rectangle.area(5.5, 7.2)
       self.assertAlmostEqual(res, 39.6)
    def test_equal_areas(self):
       res1 = rectangle.area(5, 7)
       res2 = rectangle.area(7, 5)
       self.assertEqual(res1, res2)
    # perimeter
    def test_zero_perimeter(self):
       res = rectangle.perimeter(0, 0)
       self.assertEqual(res, 0)
    def test_normal_perimeter(self):
       res = rectangle.perimeter(5, 7)
       self.assertEqual(res, 24)
    def test_normal_float_perimeter(self):
       res = rectangle.perimeter(5.5, 7.2)
       self.assertAlmostEqual(res, 25.4)
    def test_equal_perimeters(self):
       res1 = rectangle.perimeter(5, 7)
       res2 = rectangle.perimeter(7, 5)
       self.assertEqual(res1, res2)

class SquareTestCase(unittest.TestCase):
    # area
    def test_zero_area(self):
       res = square.area(0)
       self.assertEqual(res, 0)
    def test_normal_area(self):
       res = square.area(6)
       self.assertEqual(res, 36)
    def test_normal_float_area(self):
       res = square.area(6.7)
       self.assertAlmostEqual(res, 44.89)
    # perimeter
    def test_zero_perimeter(self):
       res = square.perimeter(0)
       self.assertEqual(res, 0)
    def test_normal_perimeter(self):
       res = square.perimeter(7)
       self.assertEqual(res, 28)
    def test_normal_float_perimeter(self):
       res = square.perimeter(7.7)
       self.assertAlmostEqual(res, 30.8)

class TriangleTestCase(unittest.TestCase):
    # area
    def test_zero_area(self):
       res = triangle.area(10, 0)
       self.assertEqual(res, 0)
    def test_normal_area(self):
       res = triangle.area(10, 5)
       self.assertEqual(res, 25)
    def test_normal_float_area(self):
       res = triangle.area(10.3, 5.8)
       self.assertAlmostEqual(res, 29.87)
    def test_equal_areas(self):
       res1 = triangle.area(5, 7)
       res2 = triangle.area(7, 5)
       self.assertEqual(res1, res2)
    # perimeter
    def test_zero_perimeter(self):
       res = triangle.perimeter(0, 0, 0)
       self.assertEqual(res, 0)
    def test_normal_perimeter(self):
       res = triangle.perimeter(5, 7, 4)
       self.assertEqual(res, 16)
    def test_normal_float_perimeter(self):
       res = triangle.perimeter(5.5, 7.2, 4.6)
       self.assertAlmostEqual(res, 17.3)
    def test_equal_perimeters(self):
       res1 = triangle.perimeter(5, 7, 4)
       res2 = triangle.perimeter(4, 7, 5)
       res3 = triangle.perimeter(7, 4, 5)
       self.assertEqual(res1, res2)
       self.assertEqual(res2, res3)

class TriangleTestCase(unittest.TestCase):
    # area
    def test_zero_area(self):
       res = triangle.area(10, 0)
       self.assertEqual(res, 0)
    def test_normal_area(self):
       res = triangle.area(10, 5)
       self.assertEqual(res, 25)
    def test_normal_float_area(self):
       res = triangle.area(10.3, 5.8)
       self.assertAlmostEqual(res, 29.87)
    def test_equal_areas(self):
       res1 = triangle.area(5, 7)
       res2 = triangle.area(7, 5)
       self.assertEqual(res1, res2)
    # perimeter
    def test_zero_perimeter(self):
       res = triangle.perimeter(0, 0, 0)
       self.assertEqual(res, 0)
    def test_normal_perimeter(self):
       res = triangle.perimeter(5, 7, 4)
       self.assertEqual(res, 16)
    def test_normal_float_perimeter(self):
       res = triangle.perimeter(5.5, 7.2, 4.6)
       self.assertAlmostEqual(res, 17.3)
    def test_equal_perimeters(self):
       res1 = triangle.perimeter(5, 7, 4)
       res2 = triangle.perimeter(4, 7, 5)
       res3 = triangle.perimeter(7, 4, 5)
       self.assertEqual(res1, res2)
       self.assertEqual(res2, res3)

class CircleTestCase(unittest.TestCase):
    # area
    def test_zero_area(self):
       res = circle.area(0)
       self.assertEqual(res, 0)
    def test_normal_area(self):
       res = circle.area(4)
       self.assertAlmostEqual(res, 16*math.pi)
    def test_normal_float_area(self):
       res = circle.area(4.2)
       self.assertAlmostEqual(res, 17.64*math.pi)
    # perimeter
    def test_zero_perimeter(self):
       res = circle.perimeter(0)
       self.assertEqual(res, 0)
    def test_normal_perimeter(self):
       res = circle.perimeter(4)
       self.assertAlmostEqual(res, 8*math.pi)
    def test_normal_float_perimeter(self):
       res = circle.perimeter(4.2)
       self.assertAlmostEqual(res, 8.4*math.pi)