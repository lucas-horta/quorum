This is the solution I got to for Quorum's coding challenge. It uses python 3.11 with no requirements for the main task, but it does require FastAPI for the API module as well as pytest-cov for test coverage.

## Project Structure
```
app/                              --- Application root
├─ adapters/                      --- Adapters folder
│  ├─ csv_adapter.py              --- CSV Reading and writing
├─ analysis/                      --- Main challenge features
│  ├─ bill_analysis.py            --- Generate bills.csv
│  ├─ legislator_analysis.py      --- Generate legislators-support-oppose-count.csv
├─ data/                          --- Input data
│  ├─ bills.csv
│  ├─ legislators.csv
│  ├─ vote_results.csv
│  ├─ votes.csv
├─ tests/                         --- Test coverage
│  ├─ test_bill_analysis.py       --- Test cases for bill analysis
│  ├─ test_csv_adapter.py         --- Test cases for CSV adapter
│  ├─ test_legislator_analysis.py --- Test cases for legislator analysis
├─ main.py                        --- Run the app
```

## Running locally

Requirements:
- [Git](https://git-scm.com/downloads)
- [Python3.10](https://www.python.org/downloads/)

1. Clone the repository
`git clone https://github.com/lucas-horta/quorum.git`

2. Navigate to project directory

3. Install dependencies (necessary for test coverage and API module)
`pip install -r requirements.txt`

4. Run tests
`pytest`
`pytest --cov`

5. Run the application
`python app/main.py`

6. Results will be found in project root folder:
`bills.csv`
`legislators-support-oppose-count.csv`
