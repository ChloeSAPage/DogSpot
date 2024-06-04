import sys
import os
import unittest
from unittest.mock import patch, Mock

# Add the parent directory of the project to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from yelpApi import YelpAPI
from config import API_KEY

class TestYelpAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.yelp_api = YelpAPI(API_KEY)

    @patch('yelpApi.requests.get')
    def test_get_businesses_response_is_list(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses('london')
        self.assertIsInstance(response, list)

    @patch('yelpApi.requests.get')
    def test_get_businesses_response_contains_dict(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': [{}]}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses('london')
        self.assertIsInstance(response[0], dict)

    @patch('yelpApi.requests.get')
    def test_get_businesses_no_input(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses('')
        self.assertIsInstance(response, list)

    @patch('yelpApi.requests.get')
    def test_get_businesses_strange_input(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses('pineapple')
        self.assertIsInstance(response, list)

    @patch('yelpApi.requests.get')
    def test_get_businesses_api_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {'error': 'API error'}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses('london')
        self.assertEqual(response, [])

    @patch('yelpApi.requests.get')
    def test_get_businesses_empty_response(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses('london')
        self.assertEqual(response, [])

    @patch('yelpApi.requests.get')
    def test_get_businesses_no_businesses_key(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses('london')
        self.assertEqual(response, [])

    @patch('yelpApi.requests.get')
    def test_get_businesses_by_coords_response_is_list(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses_by_coords(51.51283552118349, -0.135955810546875)
        self.assertIsInstance(response, list)

    @patch('yelpApi.requests.get')
    def test_get_businesses_by_coords_response_contains_dict(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': [{}]}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses_by_coords(51.51283552118349, -0.135955810546875)
        self.assertIsInstance(response[0], dict)

    @patch('yelpApi.requests.get')
    def test_get_businesses_by_coords_wrong_lat_long(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses_by_coords(-0.135955810546875, 51.51283552118349)
        self.assertIsInstance(response, list)

    @patch('yelpApi.requests.get')
    def test_get_businesses_by_coords_string_input(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses_by_coords("", "")
        self.assertIsInstance(response, list)

    @patch('yelpApi.requests.get')
    def test_get_businesses_by_coords_char_input(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses_by_coords("long", "lat")
        self.assertIsInstance(response, list)

    @patch('yelpApi.requests.get')
    def test_get_businesses_by_coords_out_of_range_input(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses_by_coords(500, 500)
        self.assertIsInstance(response, list)

    @patch('yelpApi.requests.get')
    def test_get_businesses_by_coords_invalid_lat_long(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'error': 'Invalid coordinates'}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses_by_coords("invalid_lat", "invalid_long")
        self.assertEqual(response, [])

    @patch('yelpApi.requests.get')
    def test_get_businesses_by_coords_api_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {'error': 'API error'}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses_by_coords(51.51283552118349, -0.135955810546875)
        self.assertEqual(response, [])

    @patch('yelpApi.requests.get')
    def test_get_businesses_by_coords_empty_response(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses_by_coords(51.51283552118349, -0.135955810546875)
        self.assertEqual(response, [])

    @patch('yelpApi.requests.get')
    def test_get_businesses_by_coords_no_businesses_key(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        response = self.yelp_api.get_businesses_by_coords(51.51283552118349, -0.135955810546875)
        self.assertEqual(response, [])

if __name__ == '__main__':
    unittest.main()
