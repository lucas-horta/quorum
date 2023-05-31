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
├─ api.py                         --- API module to retrieve results in JSON
├─ main.py                        --- Run the app
```

## Running locally

Requirements:
- [Git](https://git-scm.com/downloads)
- [Python3.11](https://www.python.org/downloads/)

1. Clone the repository
`git clone https://github.com/lucas-horta/quorum.git`

2. Navigate to project directory

3. Install dependencies (required for test coverage and API module)
`pip install -r requirements.txt`

4. Run tests
`pytest`
`pytest --cov`

5. Run the application
`python app/main.py`

6. Results will be found in project root folder:
`bills.csv`
`legislators-support-oppose-count.csv`

7. Uvicorn server will also start listening at localhost:8000/api/

GET endpoints available:
`/bill-analysis`
`/legislator-analysis`

## Quorum questions

### 1. Discuss your solution's time complexity. What tradeoffs did you make?
The solution took a heavy focus on making sure it wouldn't have too many nested for loops while reading the CSV files. However, as it's highlighted in analysis/bill_analysis.py, a three-nested for loop was necessary in order to associate the bills to their specific votes. A solution that eliminates this nesting is likely possible using entities, reducing the complexity to O(n), but it would take more time to develop, and this challenge focused on a short development time.

### 2. How would you change your solution to account for future columns that might be requested, such as "Bill Voted On Date" or "Co-Sponsors"?
Since both the reader and writer method in CSVAdapter are dynamic, they wouldn't need changes. However, the export methods on each of the analyses do need an update on their headers to accomodate for new ones.

### 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?
While the analyses mention files in their constructors, a file is not necessary to initiate them, and they could take on lists instead of files. A treatment on the adapter reader class would be necessary to accomodate for that, however, and make sure it would turn that list into the appropriate list of dictionaries that it currently returns to the analysis classes.

### 4. How lond did you spend working on the assignment?
About 5 hours.
