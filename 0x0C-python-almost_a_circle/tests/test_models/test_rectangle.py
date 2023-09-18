import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        # Create a sample Rectangle instance for testing
        self.rect = Rectangle(5, 10, 2, 3, 1)

    def test_constructor(self):
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect.height, 10)
        self.assertEqual(self.rect.x, 2)
        self.assertEqual(self.rect.y, 3)
        self.assertEqual(self.rect.id, 1)

    def test_valid_attribute(self):
        with self.assertRaises(TypeError):
            self.rect.width = "invalid"
        with self.assertRaises(ValueError):
            self.rect.width = 0

    def test_area(self):
        self.assertEqual(self.rect.area(), 5 * 10)

    def test_display(self):
        # Redirect stdout to capture print output
        from io import StringIO
        import sys
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        self.rect.display()

        # Get the printed output
        output = sys.stdout.getvalue()
        sys.stdout = saved_stdout

        expected_output = "\n" * 3 + "  #####\n" * 10

        self.assertEqual(output, expected_output)

    def test_str(self):
        self.assertEqual(str(self.rect), "[Rectangle] (1) 2/3 - 5/10")

    def test_update(self):
        self.rect.update(2, 7, 12, 4, 5)
        self.assertEqual(self.rect.id, 2)
        self.assertEqual(self.rect.width, 7)
        self.assertEqual(self.rect.height, 12)
        self.assertEqual(self.rect.x, 4)
        self.assertEqual(self.rect.y, 5)

        self.rect.update(id=3, x=1)
        self.assertEqual(self.rect.id, 3)
        self.assertEqual(self.rect.x, 1)

    def test_to_dictionary(self):
        rect_dict = self.rect.to_dictionary()
        expected_dict = {
            "id": 1,
            "width": 5,
            "height": 10,
            "x": 2,
            "y": 3
        }
        self.assertDictEqual(rect_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()
