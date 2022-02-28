import unittest
from configs.config import api_key
from geocoder_api import Client
from main.distance_calculator import find_distance_to_polygon


class Test(unittest.TestCase):
    def test_find_distance_with_address(self):
        client = Client(api_key)
        coordinates = client.transform_to_coordinates('Можайск')
        self.assertEqual(find_distance_to_polygon(coordinates), 88)


