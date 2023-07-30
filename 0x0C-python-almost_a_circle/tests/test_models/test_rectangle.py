#!/usr/bin/python3
import unittest
import models.rectangle as rectangle
import models.base as base


class TestRectangle(unittest.TestCase):

    def test_area(self):
        #test area of rectangle
        self.assertEqual(rectangle.Rectangle(2, 2).area(), 4)

    def test_print_instance(self):
        #tests proper output for print __str__
        self.assertEq




if __name__ == "__main__":
    unittest.main()
