import unittest
from csv_combiner import CsvFile


class TestCsvFile(unittest.TestCase):
    def setUp(self):
        # open two files, one for the CsvFile instance and one for our test runner
        self.file = open('fixtures/accessories.csv')
        file_copy = open('fixtures/accessories.csv')
        self.csv_file = CsvFile(file_copy)

    def test_readline(self):
        for i, line in enumerate(self.file.readlines()):
            self.assertEqual(self.csv_file.i, i)
            self.assertEqual(self.csv_file.readline(), line.rstrip())

    def test_readline_after_adding_columns(self):
        new_columns = {
            'test1': 'asdf',
            'another_column': 'another column!',
            'sample_text': '33333333333'
        }
        new_csv_header = ',"test1","another_column","sample_text"'
        new_csv = ',"asdf","another column!","33333333333"'

        for name in new_columns:
            self.csv_file.add_column(name, new_columns[name])

        for i, line in enumerate(self.file.readlines()):
            self.assertEqual(self.csv_file.i, i)

            line = line.rstrip()
            if i == 0:
                line += new_csv_header
            else:
                line += new_csv

            self.assertEqual(self.csv_file.readline(), line)

    def tearDown(self):
        # just close everything to be safe
        self.file.close()
        del self.csv_file
