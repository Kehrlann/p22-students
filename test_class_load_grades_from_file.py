import unittest
from student import Class


class TestLoadGradesFromFile(unittest.TestCase):

    def test_load_grades(self):
        p20 = Class("p1920")
        p20.load_students_from_file('class.csv')
        p20.load_grades_from_file('grades.csv')

        self.assertEqual(
            p20.get_student("Albert", "Einstein") .compute_average("Physics"),
            13.25
        )
        self.assertEqual(
            p20.get_student("Richard", "Feynman").compute_average("Physics"),
            12.
        )
        self.assertEqual(
            p20.get_student("Pierre", "Curie").compute_average("Scubadiving"),
            9.5
        )


if __name__ == '__main__':
    unittest.main()
