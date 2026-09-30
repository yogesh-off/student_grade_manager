# Tests for grading.py and reports.py
import os
import sys
import unittest

# so Python can find the files in the main folder
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grading import get_grade, get_percentage, is_pass
from reports import get_ranking, calculate_stats


class TestGrading(unittest.TestCase):

    def test_grades(self):
        self.assertEqual(get_grade(95), "A+")
        self.assertEqual(get_grade(80), "A")
        self.assertEqual(get_grade(40), "E")
        self.assertEqual(get_grade(39.9), "F")

    def test_percentage(self):
        self.assertEqual(get_percentage({"Maths": 80, "Python": 60}), 70.0)
        self.assertEqual(get_percentage({}), 0.0)

    def test_pass_and_fail(self):
        self.assertTrue(is_pass({"Maths": 40, "Python": 90}))
        self.assertFalse(is_pass({"Maths": 39, "Python": 99}))
        self.assertFalse(is_pass({}))

    def test_ranking_with_tie(self):
        data = {
            "A01": {"name": "Asha", "marks": {"Maths": 90}},
            "B01": {"name": "Bala", "marks": {"Maths": 90}},
            "C01": {"name": "Chitra", "marks": {"Maths": 60}},
            "D01": {"name": "Dev", "marks": {}},
        }
        ranked = get_ranking(data)
        self.assertEqual(len(ranked), 3)          # Dev has no marks so not ranked
        self.assertEqual(ranked[0][0], 1)
        self.assertEqual(ranked[1][0], 1)         # tie, same rank
        self.assertEqual(ranked[2][0], 3)
        self.assertEqual(ranked[2][1], "C01")

    def test_class_stats(self):
        data = {
            "A01": {"name": "Asha", "marks": {"Maths": 90}},
            "B01": {"name": "Bala", "marks": {"Maths": 30}},
        }
        stats = calculate_stats(data)
        self.assertEqual(stats["passed"], 1)
        self.assertEqual(stats["failed"], 1)
        self.assertEqual(stats["average"], 60.0)
        self.assertEqual(stats["subject_avg"]["Maths"], 60.0)

    def test_stats_with_no_marks(self):
        self.assertIsNone(calculate_stats({}))


if __name__ == "__main__":
    unittest.main()
