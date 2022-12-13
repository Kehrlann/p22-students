import unittest
from student import Student


class TestStudentName(unittest.TestCase):

    def test_student_name(self):
        achille = Student("Achille", "Talon")
        luke = Student("Lucky", "Luke")
        self.assertEqual(repr(achille), "Achille Talon")
        self.assertEqual(repr(luke), "Lucky Luke")


if __name__ == '__main__':
    unittest.main()
