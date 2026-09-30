# Tests for students.py and storage.py
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import students
from storage import load_data, save_data


class TestStudents(unittest.TestCase):

    def test_add_student(self):
        data = {}
        students.add_student(data, "S001", "Asha")
        self.assertEqual(data["S001"]["name"], "Asha")
        self.assertEqual(data["S001"]["marks"], {})

    def test_duplicate_roll_number(self):
        data = {}
        students.add_student(data, "S001", "Asha")
        with self.assertRaises(KeyError):
            students.add_student(data, "S001", "Someone Else")

    def test_update_and_delete(self):
        data = {}
        students.add_student(data, "S001", "Asha")
        students.update_name(data, "S001", "Asha Rao")
        self.assertEqual(data["S001"]["name"], "Asha Rao")
        students.delete_student(data, "S001")
        self.assertEqual(len(data), 0)

    def test_missing_student(self):
        with self.assertRaises(KeyError):
            students.get_student({}, "NOPE1")
        with self.assertRaises(KeyError):
            students.delete_student({}, "NOPE1")

    def test_set_marks(self):
        data = {}
        students.add_student(data, "S001", "Asha")
        students.set_marks(data, "S001", "Maths", 88.0)
        self.assertEqual(data["S001"]["marks"]["Maths"], 88.0)

    def test_search(self):
        data = {}
        students.add_student(data, "S001", "Asha Rao")
        self.assertEqual(len(students.search_students(data, "rao")), 1)
        self.assertEqual(len(students.search_students(data, "zzz")), 0)

    def test_save_and_load(self):
        folder = tempfile.mkdtemp()
        path = os.path.join(folder, "test.json")
        data = {"S001": {"name": "Asha", "marks": {"Maths": 50.0}}}
        save_data(data, path)
        self.assertEqual(load_data(path), data)

    def test_load_missing_or_broken_file(self):
        folder = tempfile.mkdtemp()
        self.assertEqual(load_data(os.path.join(folder, "none.json")), {})
        bad_path = os.path.join(folder, "bad.json")
        f = open(bad_path, "w")
        f.write("{this is not json")
        f.close()
        self.assertEqual(load_data(bad_path), {})


if __name__ == "__main__":
    unittest.main()
