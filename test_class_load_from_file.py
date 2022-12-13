import unittest
from student import Class


class TestLoadFromFile(unittest.TestCase):

    def test_load_from_file(self):
        p20 = Class("p1920")
        p20.load_students_from_file('class.csv')

        self.assertEqual(len(p20), 89, f"Il y a 89 élèves dans class.csv")
        self.assertIsNone(p20.get_student("Leo", "Szilard"))
        self.assertIsNotNone(p20.get_student("Tryphon", "Tournesol"))


if __name__ == '__main__':
    unittest.main()
