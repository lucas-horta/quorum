import os
import sys
# Add the project root directory to PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
import unittest
from unittest import mock
from analysis.bill_analysis import BillAnalysis

class TestBillAnalysis(unittest.TestCase):
    def setUp(self):
        self.bills_file = "bills.csv"
        self.vote_results_file = "vote_results.csv"
        self.votes_file = "votes.csv"
        self.legislators_file = "legislators.csv"
        self.bill_analysis = BillAnalysis(
            self.bills_file,
            self.vote_results_file,
            self.votes_file,
            self.legislators_file
        )

    @mock.patch("adapters.csv_adapter.CSVAdapter.read_csv")
    def test_analyze_bills(self, mock_read_csv):
        mock_read_csv.side_effect = [
            [
                {"id": "1", "title": "Bill 1", "sponsor_id": "1"},
                {"id": "2", "title": "Bill 2", "sponsor_id": None}
            ],
            [
                {"id": "1", "legislator_id": "1", "vote_id": "1", "vote_type": "1"},
                {"id": "2", "legislator_id": "2", "vote_id": "1", "vote_type": "2"},
                {"id": "3", "legislator_id": "3", "vote_id": "2", "vote_type": "1"},
                {"id": "4", "legislator_id": "1", "vote_id": "2", "vote_type": "2"}
            ],
            [
                {"id": "1", "bill_id": "1"},
                {"id": "2", "bill_id": "2"},
                {"id": "3", "bill_id": "1"},
                {"id": "4", "bill_id": "2"}
            ],
            [
                {"id": "1", "name": "Legislator A"},
                {"id": "2", "name": "Legislator B"},
                {"id": "3", "name": "Legislator C"}
            ]
        ]

        expected_result = [
            {
                "id": "1",
                "title": "Bill 1",
                "supporter_count": 1,
                "opposer_count": 1,
                "primary_sponsor": "Legislator A"
            },
            {
                "id": "2",
                "title": "Bill 2",
                "supporter_count": 1,
                "opposer_count": 1,
                "primary_sponsor": "Unknown"
            }
        ]

        result = self.bill_analysis.analyze_bills()
        self.assertEqual(result, expected_result)

    @mock.patch("adapters.csv_adapter.CSVAdapter.write_csv")
    def test_export_results(self, mock_write_csv):
        bills = [
            {
                "id": "1",
                "title": "Bill 1",
                "supporter_count": 2,
                "opposer_count": 1,
                "primary_sponsor": "Legislator A"
            },
            {
                "id": "2",
                "title": "Bill 2",
                "supporter_count": 3,
                "opposer_count": 2,
                "primary_sponsor": "Legislator B"
            }
        ]

        headers = ["id", "title", "supporter_count", "opposer_count", "primary_sponsor"]
        csv_data = [headers] + [
            ["1", "Bill 1", 2, 1, "Legislator A"],
            ["2", "Bill 2", 3, 2, "Legislator B"]
        ]

        self.bill_analysis.export_results(bills)
        mock_write_csv.assert_called_with("bills.csv", csv_data)


if __name__ == "__main__":
    unittest.main()