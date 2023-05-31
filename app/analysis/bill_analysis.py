import os
import sys
# Add the project root directory to PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
from adapters.csv_adapter import CSVAdapter
class BillAnalysis:
    def __init__(self, bills_file, vote_results_file, votes_file, legislators_file):
        self.bills_file = bills_file
        self.vote_results_file = vote_results_file
        self.votes_file = votes_file
        self.legislators_file = legislators_file

    def run_analysis(self):
        bills = self.analyze_bills()
        self.export_results(bills)

    def analyze_bills(self):
        csv_adapter = CSVAdapter()
        bills = csv_adapter.read_csv(self.bills_file)
        vote_results = csv_adapter.read_csv(self.vote_results_file)
        votes = csv_adapter.read_csv(self.votes_file)
        legislators = csv_adapter.read_csv(self.legislators_file)

        legislator_names = {
             legislator['id']: legislator['name'] for legislator in legislators
        }

        results = {}

        for bill in bills:
            sponsor_id = bill['sponsor_id']
            bill_id = bill['id']
            results[bill_id] = {
                'id': bill['id'],
                'title': bill['title'],
                'supporter_count': 0,
                'opposer_count': 0,
                'primary_sponsor': legislator_names.get(sponsor_id, 'Unknown')
            }
        
            for vote in votes:
                if bill_id == vote['bill_id']:
                    vote_id = vote['id']

                    for vote_result in vote_results:
                        if vote_id == vote_result['vote_id']:
                            vote_type = vote_result['vote_type']
                            if vote_type == '1':
                                results[bill_id]['supporter_count'] += 1
                            elif vote_type == '2':
                                results[bill_id]['opposer_count'] += 1
        return list(results.values())

    def export_results(self, bills):
        csv_adapter = CSVAdapter()
        headers = ['id', 'title', 'supporter_count', 'opposer_count', 'primary_sponsor']
        csv_data = [headers] + [[
            bill['id'],
            bill['title'],
            bill['supporter_count'],
            bill['opposer_count'],
            bill['primary_sponsor']
        ] for bill in bills]
        csv_adapter.write_csv('bills.csv', csv_data)