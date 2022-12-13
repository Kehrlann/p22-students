import unittest
from student import Student, Class


class TestGetStudent(unittest.TestCase):

    def test_exists(self):
        p20 = Class("p20")

        emmy = Student("Emmy", "Noether")
        p20.add_student(emmy)

        self.assertEqual(p20.get_student("Emmy", "Noether"), emmy)

    def test_doesnt_exist(self):
        p20 = Class("p20")

        emmy = Student("Emmy", "Noether")
        p20.add_student(emmy)

        self.assertIsNone(p20.get_student("Margaret", "Hamilton"))


if __name__ == '__main__':
    unittest.main()
