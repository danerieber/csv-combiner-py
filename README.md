# csv-combiner-py

Combines rows from multiple CSV files into one CSV file, adding a column specifying the original file for each row.

## Other Features

You may use the `csv_combiner.util.CsvFile` class to extend upon this and add your own columns. Note that this only adds a column that is filled with a constant value.

## Note

See `src/csv_combiner/__main__.py` for main function and `src/csv_combiner/util/util.py` for `CsvFile` class.