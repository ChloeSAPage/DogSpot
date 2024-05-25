import requests
from config import API_KEY

location = "london"

url = f"https://api.yelp.com/v3/businesses/search?location={location}&term=Dogs+Friendly"

headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}

response = requests.get(url, headers=headers)

result = response.json()

businesses = result["businesses"]

for business in businesses:
    print(business["name"])