import unittest
from unittest.mock import patch

import pandas as pd

from src.csv_xlsx_reader import read_csv_transactions, read_excel_transactions


class TestTransactionFunctions(unittest.TestCase):

    @patch("os.path.exists")
    @patch("pandas.read_csv")
    def test_read_csv_transactions(self, mock_read_csv, mock_exists):
        mock_exists.return_value = True
        mock_read_csv.return_value = pd.DataFrame({"column1": [1, 2], "column2": ["a", "b"]})

        result = read_csv_transactions("dummy_path.csv")
        expected_result = [{"column1": 1, "column2": "a"}, {"column1": 2, "column2": "b"}]
        self.assertEqual(result, expected_result)

    @patch("os.path.exists")
    @patch("pandas.read_excel")
    def test_read_excel_transactions(self, mock_read_excel, mock_exists):
        mock_exists.return_value = True
        mock_read_excel.return_value = pd.DataFrame({"column1": [3, 4], "column2": ["c", "d"]})

        result = read_excel_transactions("dummy_path.xlsx")
        expected_result = [{"column1": 3, "column2": "c"}, {"column1": 4, "column2": "d"}]
        self.assertEqual(result, expected_result)

    @patch("os.path.exists")
    def test_read_csv_file_not_found(self, mock_exists):
        mock_exists.return_value = False
        result = read_csv_transactions("dummy_path.csv")
        self.assertEqual(result, [])

    @patch("os.path.exists")
    def test_read_excel_file_not_found(self, mock_exists):
        mock_exists.return_value = False
        result = read_excel_transactions("dummy_path.xlsx")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
