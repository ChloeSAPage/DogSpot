from unittest import TestCase, main
from yelpApi import YelpAPI
from config import API_KEY


class TestGetBusinesses(TestCase):

    def setUp(self):
        self.yelpAPI = YelpAPI(API_KEY)

    def test_response_is_list(self):
        expected = type([])
        result = type(self.yelpAPI.get_businesses('london'))
        self.assertEqual(expected, result)

    def test_response_contains_dict(self):
        expected = type({})
        result = type(self.yelpAPI.get_businesses('london')[0])
        self.assertEqual(expected, result)

    def test_no_input(self):
        # technically you can't put no input but sneaky cybersecurity people might be able to
        expected = type([])
        result = type(self.yelpAPI.get_businesses(''))
        self.assertEqual(expected, result)

    def test_strange_input(self):
        expected = type([])
        result = type(self.yelpAPI.get_businesses('pineapple'))
        self.assertEqual(expected, result)


class TestGetBusinessesByCoords(TestCase):

    def setUp(self):
        self.yelpAPI = YelpAPI(API_KEY)

    def test_response_is_list(self):
        expected = type([])
        result = type(self.yelpAPI.get_businesses_by_coords(51.51283552118349, -0.135955810546875))
        self.assertEqual(expected, result)

    def test_response_contains_dict(self):
        expected = type({})
        result = type(self.yelpAPI.get_businesses_by_coords(51.51283552118349, -0.135955810546875)[0])
        self.assertEqual(expected, result)

    def test_wrong_lat_long(self):
        expected = type([])
        result = type(self.yelpAPI.get_businesses_by_coords(-0.135955810546875, 51.51283552118349))
        self.assertEqual(expected, result)

    def test_string_input(self):
        expected = type([])
        result = type(self.yelpAPI.get_businesses_by_coords("", ""))
        self.assertEqual(expected, result)

    def test_char_input(self):
        expected = type([])
        result = type(self.yelpAPI.get_businesses_by_coords("long", "lat"))
        self.assertEqual(expected, result)

    def test_out_of_range_input(self):
        expected = type([])
        result = type(self.yelpAPI.get_businesses_by_coords(500, 500))
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()