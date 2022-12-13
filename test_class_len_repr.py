import unittest
from student import Student, Class


class TestClassLenRepr(unittest.TestCase):

    def test_class_len(self):
        zero = Class("zero")
        one = Class("one")
        many = Class("many")

        one.add_student(Student("Maria", "Merian"))
        many.add_student(Student("Ada", "Lovelace"))
        many.add_student(Student("Charles", "Babbage"))

        self.assertEqual(len(zero), 0)
        self.assertEqual(len(one), 1)
        self.assertGreater(len(many), 1)

    def test_class_repr(self):
        zero = Class("zero")
        one = Class("one")
        many = Class("many")

        one.add_student(Student("Maria", "Merian"))
        many.add_student(Student("Ada", "Lovelace"))
        many.add_student(Student("Charles", "Babbage"))

        self.assertEqual(repr(zero), "Class zero - 0 student(s)")
        self.assertEqual(repr(one), "Class one - 1 student(s)")
        self.assertEqual(repr(many), "Class many - 2 student(s)")


if __name__ == '__main__':
    unittest.main()
