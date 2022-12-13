import unittest
from student import Student


class TestReport(unittest.TestCase):

    def test_report_achille(self):
        albert = Student("Albert", "Einstein")
        albert.add_grade("Mathematics", 12.80)
        albert.add_grade("Scubadiving", 12.50)
        report = (f'Report for student Albert Einstein\n'
                  f'+===============+===============+\n'
                  f'|     Topic     |    Average    |\n'
                  f'+===============+===============+\n'
                  f'|  Mathematics  |     12.80     |\n'
                  f'+---------------+---------------+\n'
                  f'|  Scubadiving  |     12.50     |\n'
                  f'+---------------+---------------+\n'
                  )
        self.assertEqual(albert.report(), report)

    def test_report_luke(self):
        luke = Student("Lucky", "Luke")
        luke.add_grade("English", 10.)
        luke.add_grade("English", 12.)
        luke.add_grade("French", 12.50)

        report_lines = luke.report().split("\n")

        self.assertEqual(report_lines[0], 'Report for student Lucky Luke')
        self.assertRegex(report_lines[4], r'\|\s*English\s*\|\s*11\.00\s*\|')
        self.assertRegex(report_lines[6], r'\|\s*French\s*\|\s*12\.50\s*\|')


if __name__ == '__main__':
    unittest.main()
