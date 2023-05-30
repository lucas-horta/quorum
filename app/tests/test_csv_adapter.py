import os
import sys
# Add the project root directory to PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
import unittest
from unittest.mock import patch, mock_open
from adapters.csv_adapter import CSVAdapter

class TestCSVAdapter(unittest.TestCase):
    def setUp(self):
        self.csv_adapter = CSVAdapter()

    def test_read_csv(self):
        expected_result = [
            {'id': '1', 'name': 'John'},
            {'id': '2', 'name': 'Jane'}
        ]
        with patch('builtins.open', new_callable=mock_open, read_data='id,name\n1,John\n2,Jane\n') as mock_file:
            result = self.csv_adapter.read_csv('test.csv')
            self.assertEqual(result, expected_result)
            mock_file.assert_called_once_with('test.csv', 'r', newline='')

    def test_write_csv(self):
        data = [
            ['id', 'name'],
            ['1', 'John'],
            ['2', 'Jane']
        ]

        self.csv_adapter.write_csv('test.csv', data)
        result = self.csv_adapter.read_csv('test.csv')
        expected_result = [{'id': '1', 'name': 'John'}, {'id': '2', 'name': 'Jane'}]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()