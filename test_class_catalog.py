
import unittest
from student import Class


class TestCatalog(unittest.TestCase):

    def test_catalog(self):
        p20 = Class("p1920")
        p20.load_students_from_file('class.csv')
        p20.load_grades_from_file('grades.csv')

        true_catalog = {'Physics': 89, 'Mathematics': 89, 'Chemistry': 89, 
                'English': 69, 'French': 30, 'Scubadiving': 10, 'Horse-riding': 15, 'Sailing': 3}

        catalog = p20.catalog()
        self.assertIsInstance(catalog, dict)
        self.assertEqual(true_catalog, dict(catalog))


if __name__ == '__main__':
    unittest.main()
