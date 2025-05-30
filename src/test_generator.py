import unittest
from generator import extract_title

class TestPageGenerator(unittest.TestCase):
    def test_valid_title(self):
        md = "# Hello World"
        self.assertEqual(extract_title(md), "Hello World")

    def test_title_with_whitespace(self):
        md = "#     Trim me   "
        self.assertEqual(extract_title(md), "Trim me")

    def test_missing_title(self):
        md = "No title here"
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()
