#!/usr/bin/python3
"""
unit test Base classsssss
"""
import unittest
import models.base as b
Base = b.Base

class TestBase(unittest.TestCase):

    def test_constructor_with_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_constructor_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_non_empty_list(self):
        data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]')

    def test_save_to_file_empty_list(self):
        with open('Base.json', 'w') as file:
            file.write('')
        Base.save_to_file([])
        with open('Base.json', 'r') as file:
            file_contents = file.read()
        self.assertEqual(file_contents, '[]')
    """
    def test_save_to_file_non_empty_list(self):
        data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        with open('Base.json', 'w') as file:
            file.write('')
        Base.save_to_file(data)
        with open('Base.json', 'r') as file:
            file_contents = file.read()
        self.assertEqual(file_contents, '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]')
    """
    
if __name__ == "__main__":
    unittest.main()

