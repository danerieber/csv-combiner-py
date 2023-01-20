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
