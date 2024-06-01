import requests

class YelpAPI:
    def __init__(self, API_KEY) -> None:
        self.baseurl = "https://api.yelp.com/v3/businesses/search?"
        self.headers =  {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}

    def get_businesses(self, location):
        url = f"{self.baseurl}location={location}&term=Dogs+Friendly"
        response = requests.get(url, headers=self.headers)

        # Log the status code and the JSON response for debugging
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")

        result = response.json()
        # Check if 'businesses' key exists in the result
        if 'businesses' in result:
            return result['businesses']
        else:
            # Handle the case where 'businesses' key is not present
            print("Error: 'businesses' key not found in the response.")
            return []

    def get_businesses_by_coords(self, latitude, longitude):
        url = f"{self.baseurl}latitude={latitude}&longitude={longitude}&term=Dogs+Friendly"
        response = requests.get(url, headers=self.headers)

        # Log the status code and the JSON response for debugging
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")

        result = response.json()
        # Check if 'businesses' key exists in the result
        if 'businesses' in result:
            return result['businesses']
        else:
            # Handle the case where 'businesses' key is not present
            print("Error: 'businesses' key not found in the response.")
            return []