import argparse
from pathlib import Path


def get_parser():
    """Define command line arguments

    Returns:
        ArgumentParser: Parse arguments with .parse_args()
    """
    parser = argparse.ArgumentParser(
        prog='CSV Combiner',
        description='Combines rows from multiple CSV files into one CSV file, '
                    'adding a column specifying the original file for each row'
    )
    parser.add_argument(
        'files', nargs='+', type=argparse.FileType('r'), help='Specify input CSV files')
    return parser


class CsvFile:
    """Wrapper for a CSV file that can add columns filled with a single value
    """

    def __init__(self, file):
        self.file = file
        self.added_columns = {}
        self.i = 0

    def __del__(self):
        self.file.close()

    def add_column(self, name, value):
        """Add a new column

        Args:
            name (str): The name of the column (for the CSV header)
            value (str): Fill the new column with the specified value
        """
        self.added_columns[name] = value

    def readline(self):
        """Read the next line from the CSV file

        Returns:
            str: The next line with any added columns
        """
        line = self.file.readline().rstrip()
        if line:
            for name in self.added_columns:
                if self.i == 0:
                    line += f',"{name}"'    # CSV header
                else:
                    line += f',"{self.added_columns[name]}"'
            self.i += 1
        return line


def print_rows(csv_file, print_header=True):
    """Prints every row in a CsvFile

    Args:
        csv_file (_type_): A CsvFile instance
        print_header (bool, optional): Only prints the CSV header when True. Defaults to True.
    """
    if not print_header:
        csv_file.readline()
    while line := csv_file.readline():
        print(line)


def main():
    """Print each CSV file's contents with added "filename" column
    """
    args = get_parser().parse_args()
    for i, file in enumerate(args.files):
        filename = Path(file.name).name
        csv_file = CsvFile(file)
        csv_file.add_column("filename", filename)
        print_rows(csv_file, i == 0)    # only print header for first file


if __name__ == '__main__':
    main()
