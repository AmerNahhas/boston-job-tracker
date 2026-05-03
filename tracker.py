# Boston Job Tracker v3 - by Amer Nahhas
# Using Greenhouse API to pull actual job titles

import requests
import pandas as pd
from datetime import date

companies = [
    {"name": "HubSpot", "token": "hubspotjobs"},
    {"name": "Klaviyo", "token": "klaviyo"},
    {"name": "DraftKings", "token": "draftkings"},
    {"name": "Cogito", "token": "cogitocorp"},
    {"name": "Brightcove", "token": "brightcove"},
    {"name": "CarGurus", "token": "cargurus"},
    {"name": "Recorded Future", "token": "recordedfuture"},
    {"name": "Acquia", "token": "acquia"},
    {"name": "Rapid7", "token": "rapid7"},
    {"name": "Smartsheet", "token": "smartsheet"},
    {"name": "Markforged", "token": "markforged"},
    {"name": "Toast", "token": "toasttab"},
    {"name": "Chewy", "token": "chewy"},
    {"name": "TripAdvisor", "token": "tripadvisor"},
    {"name": "Drift", "token": "drift"}
]

keywords = [
    "operations",
    "coordinator",
    "analyst",
    "project manager",
    "program manager",
    "logistics",
    "business operations",
    "revenue operations",
    "people operations"
]

results = []

for company in companies:
    print("Checking: " + company["name"] + "...")
    url = "https://boards-api.greenhouse.io/v1/boards/" + company["token"] + "/jobs"
    
    try:
        response = requests.get(url)
        data = response.json()
        jobs = data.get("jobs", [])
        
        matched_jobs = []
        for job in jobs:
            title = job["title"].lower()
            for keyword in keywords:
                if keyword in title:
                    matched_jobs.append(job["title"])
                    break
        
        if matched_jobs:
            status = "✅ " + str(len(matched_jobs)) + " roles found"
            print(status)
            for job in matched_jobs:
                print("  → " + job)
        else:
            status = "⚠️ No matching roles"
            print(status)
            
    except:
        status = "❌ Could not reach"
        print(status)
    
    results.append({
        "Company": company["name"],
        "Matching Roles": ", ".join(matched_jobs) if matched_jobs else "None",
        "Total Matches": len(matched_jobs) if matched_jobs else 0,
        "Status": status,
        "Date Checked": date.today()
    })
    print("---")

df = pd.DataFrame(results)
df.to_excel("job_tracker_results.xlsx", index=False)
print("✅ Results saved to job_tracker_results.xlsx")