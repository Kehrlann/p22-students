
import unittest
from student import Class


class TestComputeAverages(unittest.TestCase):

    def test_compute_averages(self):
        p20 = Class("p1920")
        p20.load_students_from_file('class.csv')
        p20.load_grades_from_file('grades.csv')

        true_averages = {'Physics': 12.053370786516854,
                         'Mathematics': 12.071910112359552,
                         'Chemistry': 11.977528089887638,
                         'English': 12.369565217391305,
                         'French': 11.683333333333334,
                         'Scubadiving': 11.7,
                         'Horse-riding': 11.366666666666667,
                         'Sailing': 14.0}

        avgs = p20.compute_averages()
        for topic, average in avgs.items():
            self.assertAlmostEqual(average, true_averages[topic])


if __name__ == '__main__':
    unittest.main()
