# Tests for validators.py
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from validators import check_roll, check_name, check_subject, check_marks


class TestValidators(unittest.TestCase):

    def test_roll_ok(self):
        self.assertEqual(check_roll(" 24bce001 "), "24BCE001")

    def test_roll_bad(self):
        for bad in ["", "ab", "has space", "a-b-c"]:
            with self.assertRaises(ValueError):
                check_roll(bad)

    def test_name_ok(self):
        self.assertEqual(check_name("  rahul   sharma "), "Rahul Sharma")

    def test_name_bad(self):
        for bad in ["R", "1234", "a<b>"]:
            with self.assertRaises(ValueError):
                check_name(bad)

    def test_subject(self):
        self.assertEqual(check_subject("python  basics"), "Python Basics")
        with self.assertRaises(ValueError):
            check_subject("x")

    def test_marks_ok(self):
        self.assertEqual(check_marks("87.5"), 87.5)
        self.assertEqual(check_marks("0"), 0)
        self.assertEqual(check_marks("100"), 100)

    def test_marks_bad(self):
        for bad in ["-1", "101", "abc", "nan"]:
            with self.assertRaises(ValueError):
                check_marks(bad)


if __name__ == "__main__":
    unittest.main()
