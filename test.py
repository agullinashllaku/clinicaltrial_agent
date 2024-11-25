import requests

# Base URL for the API
base_url = "https://clinicaltrials.gov/api/v2/studies?format=csv&query.cond=%28head+OR+neck%29+AND+pain&filter.advanced=heart+attack+AND+SEARCH%5BLocation%5D%28AREA%5BLocationCountry%5DUnited+States+AND+AREA%5BLocationStatus%5DRecruiting%29"

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
