import requests
from config import API_KEY

location = "london"

url = f"https://api.yelp.com/v3/businesses/search?location={location}&term=Dogs+Friendly"

headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}

response = requests.get(url, headers=headers)

result = response.json()

businesses = result["businesses"]

for business in businesses:
    # print(business["name"])
    # print(f"{business.keys()} \n")
    print(f"{business["coordinates"]} \n")

    # Name
    # rating
    # coordinates
    # display_address

    # All the info we can use
    # dict_keys(['id', 'alias', 'name', 'image_url', 'is_closed', 'url', 'review_count', 'categories', 'rating', 'coordinates', 'transactions', 'price', 'location', 'phone', 'display_phone', 'distance', 'attributes'])