import unittest
from student import Student


def topics_as_set(student):
    return set(student.followed_topics())


Student._topics_as_set = topics_as_set


class TestStudentTopics(unittest.TestCase):

    def test_one_topic(self):
        student = Student("a", "b")
        student.add_grade("Math", 12.)
        student.add_grade("Math", 14.)
        self.assertEqual(student._topics_as_set(), {"Math"})

    def test_many_topics(self):
        student = Student("a", "b")
        student.add_grade("Math", 12.)
        student.add_grade("History", 14.)
        student.add_grade("French", 10.)
        self.assertEqual(
            student._topics_as_set(),
            {"History", "French", "Math"}
        )

    def test_no_topics(self):
        student = Student("a", "b")
        self.assertEqual(len(student.followed_topics()), 0)


if __name__ == '__main__':
    unittest.main()
