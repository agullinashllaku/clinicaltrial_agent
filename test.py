import requests

# Base URL for the API
base_url = "https://clinicaltrials.gov/api/v2/studies?format=csv&query.cond=%22persistent+neck+pain%22+AND+stiffness+AND+discomfort&filter.overallStatus=NOT_YET_RECRUITING%7CRECRUITING&postFilter.advanced=AREA%5BMinimumAge%5DRANGE%5BMIN%2C+50+years%5D&fields=NCT+Number%7CStudy+Title%7CStudy+URL%7CBrief+Summary%7CPrimary+Outcome+Measures%7CConditions%7CInterventions%7CPhases%7CLocations"

# Sending the GET request
response = requests.get(base_url)

# Checking the response
if response.status_code == 200:
    data = response
    # Loop through studies and print their keys (column names)
    for study in data:
        print(study)  # Use .keys() to retrieve dictionary keys

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
