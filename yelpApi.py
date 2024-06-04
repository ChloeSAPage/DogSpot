import requests

class YelpAPI:
    def __init__(self, API_KEY, test_config=None) -> None:
        if test_config:
            self.app.config.update(test_config)
        self.baseurl = "https://api.yelp.com/v3/businesses/search?"
        self.headers =  {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}

#function for user inputted location requested to yelp api
    def get_businesses(self, location):
        url = f"{self.baseurl}location={location}&term=Dogs+Friendly&open_now=true&sort_by=distance"
        response = requests.get(url, headers=self.headers)
        print(f"Status Code: {response.status_code}")
        result = response.json()
        if 'businesses' in result:
            return result['businesses']
        else:
            print("Error: 'businesses' key not found in the response.")
            return []

#function for geolocation requesting to yelp api
    def get_businesses_by_coords(self, latitude, longitude):
        url = f"{self.baseurl}latitude={latitude}&longitude={longitude}&term=Dogs+Friendly&open_now=true&sort_by=distance"
        response = requests.get(url, headers=self.headers)
        print(f"Status Code: {response.status_code}")
        result = response.json()
        if 'businesses' in result:
            return result['businesses']
        else:
            print("Error: 'businesses' key not found in the response.")
            return []