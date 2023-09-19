import unittest
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):

    def setUp(self):
        # Create a sample Square instance for testing
        self.square = Square(5, 2, 3, 1)

    def test_constructor(self):
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 1)

    def test_size_property(self):
        self.assertEqual(self.square.size, 5)
        self.square.size = 7
        self.assertEqual(self.square.size, 7)

    def test_str(self):
        self.assertEqual(str(self.square), "[Square] (1) 2/3 - 5")

    def test_update(self):
        self.square.update(2, 8, 4, 5)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 5)

        self.square.update(id=3, x=1)
        self.assertEqual(self.square.id, 3)
        self.assertEqual(self.square.x, 1)

    def test_to_dictionary(self):
        square_dict = self.square.to_dictionary()
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertDictEqual(square_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()

