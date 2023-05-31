import os
import sys
# Add the project root directory to PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
from fastapi import FastAPI
from analysis.bill_analysis import BillAnalysis
from analysis.legislator_analysis import LegislatorAnalysis

app = FastAPI()

# Get files from data folder
legislators_file = os.path.join(
    os.path.dirname(__file__), 'data', 'legislators.csv')
vote_results_file = os.path.join(
    os.path.dirname(__file__), 'data', 'vote_results.csv')
votes_file = os.path.join(
    os.path.dirname(__file__), 'data', 'votes.csv')
bills_file = os.path.join(
    os.path.dirname(__file__), 'data', 'bills.csv')

@app.get('/bill-analysis')
def get_bill_analysis():
    bill_analysis = BillAnalysis(bills_file, vote_results_file, votes_file, legislators_file)
    analysis_results = bill_analysis.analyze_bills()
    return analysis_results

@app.get('/legislator-analysis')
def get_legislator_analysis():
    legislator_analysis = LegislatorAnalysis(legislators_file, vote_results_file)
    analysis_results = legislator_analysis.analyze_legislators()
    return analysis_results