import os
import sys
# Add the project root directory to PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
import unittest
from unittest.mock import patch, mock_open
from analysis.legislator_analysis import LegislatorAnalysis

class TestLegislatorAnalysis(unittest.TestCase):
    def test_analyze_legislators(self):
        legislators_file = "legislators.csv"
        vote_results_file = "vote_results.csv"
        
        csv_adapter_mock = patch("analysis.legislator_analysis.CSVAdapter").start()
        csv_adapter_instance = csv_adapter_mock.return_value
        csv_adapter_instance.read_csv.side_effect = [
            [
                {"id": "1", "name": "John"},
                {"id": "2", "name": "Jane"}
            ],
            [
                {"legislator_id": "1", "vote_type": "1"},
                {"legislator_id": "2", "vote_type": "2"},
                {"legislator_id": "1", "vote_type": "1"}
            ]
        ]
        
        legislator_analysis = LegislatorAnalysis(legislators_file, vote_results_file)
        result = legislator_analysis.analyze_legislators()
        
        expected_result = [
            {
                "id": "1",
                "name": "John",
                "num_supported_bills": 2,
                "num_opposed_bills": 0
            },
            {
                "id": "2",
                "name": "Jane",
                "num_supported_bills": 0,
                "num_opposed_bills": 1
            }
        ]
        
        self.assertEqual(result, expected_result)
        csv_adapter_instance.read_csv.assert_any_call(legislators_file)
        csv_adapter_instance.read_csv.assert_any_call(vote_results_file)
        
        patch.stopall()

    def test_export_results(self):
        legislator_votes = [
            {
                "id": "1",
                "name": "John",
                "num_supported_bills": 2,
                "num_opposed_bills": 0
            },
            {
                "id": "2",
                "name": "Jane",
                "num_supported_bills": 0,
                "num_opposed_bills": 1
            }
        ]
        
        csv_adapter_mock = patch("analysis.legislator_analysis.CSVAdapter").start()
        csv_adapter_instance = csv_adapter_mock.return_value
        
        legislator_analysis = LegislatorAnalysis("legislators.csv", "vote_results.csv")
        legislator_analysis.export_results(legislator_votes)
        
        expected_csv_data = [
            ["id", "name", "num_supported_bills", "num_opposed_bills"],
            ["1", "John", 2, 0],
            ["2", "Jane", 0, 1]
        ]
        
        csv_adapter_instance.write_csv.assert_called_with("legislators-support-oppose-count.csv", expected_csv_data)
        
        patch.stopall()

if __name__ == "__main__":
    unittest.main()
