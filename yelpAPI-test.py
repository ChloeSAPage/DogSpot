import unittest
from unittest.mock import patch, Mock
from app import App

class TestGetBusinesses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app_instance = App()
        cls.client = cls.app_instance.app.test_client()

    @patch('app.requests.get')
    def test_response_is_list(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses('london')
        self.assertIsInstance(response, list)

    @patch('app.requests.get')
    def test_response_contains_dict(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': [{}]}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses('london')
        self.assertIsInstance(response[0], dict)

    @patch('app.requests.get')
    def test_no_input(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses('')
        self.assertIsInstance(response, list)

    @patch('app.requests.get')
    def test_strange_input(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses('pineapple')
        self.assertIsInstance(response, list)

    @patch('app.requests.get')
    def test_api_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {'error': 'API error'}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses('london')
        self.assertEqual(response, [])

    @patch('app.requests.get')
    def test_empty_response(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses('london')
        self.assertEqual(response, [])

    @patch('app.requests.get')
    def test_no_businesses_key(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses('london')
        self.assertEqual(response, [])


class TestGetBusinessesByCoords(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app_instance = App()
        cls.client = cls.app_instance.app.test_client()

    @patch('app.requests.get')
    def test_response_is_list(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses_by_coords(51.51283552118349, -0.135955810546875)
        self.assertIsInstance(response, list)

    @patch('app.requests.get')
    def test_response_contains_dict(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': [{}]}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses_by_coords(51.51283552118349, -0.135955810546875)
        self.assertIsInstance(response[0], dict)

    @patch('app.requests.get')
    def test_wrong_lat_long(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses_by_coords(-0.135955810546875, 51.51283552118349)
        self.assertIsInstance(response, list)

    @patch('app.requests.get')
    def test_string_input(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses_by_coords("", "")
        self.assertIsInstance(response, list)

    @patch('app.requests.get')
    def test_char_input(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses_by_coords("long", "lat")
        self.assertIsInstance(response, list)

    @patch('app.requests.get')
    def test_out_of_range_input(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses_by_coords(500, 500)
        self.assertIsInstance(response, list)

    @patch('app.requests.get')
    def test_invalid_lat_long(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'error': 'Invalid coordinates'}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses_by_coords("invalid_lat", "invalid_long")
        self.assertEqual(response, [])

    @patch('app.requests.get')
    def test_api_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {'error': 'API error'}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses_by_coords(51.51283552118349, -0.135955810546875)
        self.assertEqual(response, [])

    @patch('app.requests.get')
    def test_empty_response(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'businesses': []}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses_by_coords(51.51283552118349, -0.135955810546875)
        self.assertEqual(response, [])

    @patch('app.requests.get')
    def test_no_businesses_key(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        response = self.app_instance.get_businesses_by_coords(51.51283552118349, -0.135955810546875)
        self.assertEqual(response, [])

if __name__ == '__main__':
    unittest.main()
