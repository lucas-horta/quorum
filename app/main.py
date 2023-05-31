import os
import sys
# Add the project root directory to PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
from analysis.bill_analysis import BillAnalysis
from analysis.legislator_analysis import LegislatorAnalysis
from fastapi import FastAPI
from app.api import app as api_app

app = FastAPI()

app.mount("/api", api_app)

if __name__ == "__main__":

    # Get files from data folder
    legislators_file = os.path.join(
        os.path.dirname(__file__), 'data', 'legislators.csv')
    vote_results_file = os.path.join(
        os.path.dirname(__file__), 'data', 'vote_results.csv')
    votes_file = os.path.join(
        os.path.dirname(__file__), 'data', 'votes.csv')
    bills_file = os.path.join(
        os.path.dirname(__file__), 'data', 'bills.csv')

    # Run analysis for bills
    bills_analysis = BillAnalysis(
        bills_file, vote_results_file,
        votes_file,legislators_file)
    bills_analysis.run_analysis()

    # Run analysis for legislators
    legislators_analysis = LegislatorAnalysis(
        legislators_file, vote_results_file
    )
    legislators_analysis.run_analysis()

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)