import unittest
from student import Student


class TestStudentTopics(unittest.TestCase):

    def test_one_grade(self):
        student = Student("a", "b")
        student.add_grade("Math", 12.)
        self.assertEqual(student.compute_average("Math"), 12.)

    def test_many_grades(self):
        student = Student("a", "b")
        grades = [8., 10., 12., 12.]
        for grade in grades:
            student.add_grade("History", grade)
        self.assertEqual(
            student.compute_average("History"),
            10.5,
            f"for grades {grades}, average should be 10.5")

    def test_missing_topic(self):
        student = Student("a", "b")
        self.assertEqual(
            student.compute_average("Unknown topic"),
            -1.,
            f"when student hasn't studied a topic, average should be -1"
        )


if __name__ == '__main__':
    unittest.main()
