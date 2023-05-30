import os
import sys
# Add the project root directory to PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
from adapters.csv_adapter import CSVAdapter

class LegislatorAnalysis:
    def __init__(self, legislators_file, vote_results_file):
        self.legislators_file = legislators_file
        self.vote_results_file = vote_results_file

    def run_analysis(self):
        legislator_votes = self.analyze_legislators()
        self.export_results(legislator_votes)

    def analyze_legislators(self):
        csv_adapter = CSVAdapter()
        
        legislators = csv_adapter.read_csv(self.legislators_file)
        vote_results = csv_adapter.read_csv(self.vote_results_file)
        
        legislator_votes = {}

        for legislator in legislators:
            legislator_id = legislator["id"]
            legislator_votes[legislator_id] = {
                "id": legislator_id,
                "name": legislator["name"],
                "num_supported_bills": 0,
                "num_opposed_bills": 0
            }

        for vote_result in vote_results:
            vote_type = vote_result["vote_type"]
            if vote_type == "1":
                legislator_votes[vote_result["legislator_id"]]["num_supported_bills"] += 1
            elif vote_type == "2":
                legislator_votes[vote_result["legislator_id"]]["num_opposed_bills"] += 1

        return list(legislator_votes.values())

    def export_results(self, legislator_votes):
        csv_adapter = CSVAdapter()
        headers = ["id", "name", "num_supported_bills", "num_opposed_bills"]
        csv_data = [headers] + [[
            legislator["id"],
            legislator["name"],
            legislator["num_supported_bills"],
            legislator["num_opposed_bills"]
        ] for legislator in legislator_votes]
        print(csv_data)
        csv_adapter.write_csv("legislators-support-oppose-count.csv", csv_data)


def main():
    legislators_file = os.path.join(os.path.dirname(__file__), '..', 'data', '', 'legislators.csv')
    vote_results_file = os.path.join(os.path.dirname(__file__), '..', 'data', '', 'vote_results.csv')
    runner = LegislatorAnalysis(legislators_file, vote_results_file)
    runner.run_analysis()

if __name__ == "__main__":
    main()