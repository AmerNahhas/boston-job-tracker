# Boston Job Tracker 🗺️

A Python automation tool that queries the Greenhouse API to find real job openings at 15+ Boston-area companies and exports results to a timestamped Excel report.

## What it does
- Connects directly to the Greenhouse Jobs API for each target company
- Searches job titles for ops-related keywords in real time
- Returns actual job titles — not just keyword matches on a webpage
- Exports results to Excel with company, roles found, match count, and date

## Built with
- Python 3.14
- requests — API calls to Greenhouse
- pandas — organizes and exports data to Excel
- openpyxl — writes the .xlsx file

## Target Companies
HubSpot, Klaviyo, DraftKings, Cogito, Brightcove, CarGurus, Recorded Future, Acquia, Rapid7, Smartsheet, Markforged, Toast, Chewy, TripAdvisor, Drift

## How to run
1. Install dependencies: `pip3 install requests pandas openpyxl`
2. Run the script: `python3 tracker.py`
3. Open `job_tracker_results.xlsx` to see results

## Sample Output
- Klaviyo → 16 roles including Workplace & Real Estate Operations Manager
- CarGurus → 9 roles including Senior Project Manager
- Smartsheet → 13 roles including Sr. Revenue Operations Analyst
- TripAdvisor → 6 roles including Business Operations Manager

## Author
Amer Nahhas — Operations & Data
