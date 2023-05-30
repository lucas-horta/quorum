import os
import sys
# Add the project root directory to PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
import unittest
from adapters.csv_adapter import CSVAdapter

class TestCSVAdapter(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_data.csv"
        self.adapter = CSVAdapter()

    def tearDown(self):
        # Clean up the test data file after each test
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_read_csv(self):
        # Create a test data file
        data = [
            {"Header1": "Value1", "Header2": "Value2"},
            {"Header1": "Value3", "Header2": "Value4"}
        ]
        self.adapter.write_csv(self.file_path, data)

        # Read the test data file using the CSVAdapter
        result = self.adapter.read_csv(self.file_path)

        # Assert the expected data
        expected_result = [
            {"Header1": "Value1", "Header2": "Value2"},
            {"Header1": "Value3", "Header2": "Value4"}
        ]
        self.assertEqual(result, expected_result)

    def test_write_csv(self):
        # Prepare test data
        data = [
            {"Header1": "Value1", "Header2": "Value2"},
            {"Header1": "Value3", "Header2": "Value4"}
        ]

        # Write the test data to a CSV file using the CSVAdapter
        self.adapter.write_csv(self.file_path, data)

        # Read the written CSV file to verify its content
        result = self.adapter.read_csv(self.file_path)

        # Assert the expected CSV content
        expected_result = [
            {"Header1": "Value1", "Header2": "Value2"},
            {"Header1": "Value3", "Header2": "Value4"}
        ]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
