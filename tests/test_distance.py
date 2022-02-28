import unittest
from decimal import Decimal

from configs.config import api_key
from geocoder_api import Client
from main.distance_calculator import find_distance_to_polygon


# client = Client(api_key)
# lat, lon = Decimal(54.719362), Decimal(20.505681)
# print(find_distance_to_polygon((lat, lon)))

class Test(unittest.TestCase):
    def test_find_distance_with_address(self):
        client = Client(api_key)
        coordinates = client.transform_to_coordinates('Можайск')
        self.assertEqual(find_distance_to_polygon(coordinates), 88)

    def test_find_distance_with_coordinates(self):
        lat, lon = Decimal(54.719362), Decimal(20.505681)
        self.assertEqual(find_distance_to_polygon((lat, lon)), 1072)

    def address_inside_mkad(self):
        client = Client(api_key)
        coordinates = client.transform_to_coordinates('Красная площадь')
        self.assertEqual(find_distance_to_polygon(coordinates), 'Точка находится внутри МКАДа!')

    def coordinates_inside_mkad(self):
        lat, lon = Decimal(55.781205), Decimal(37.599525)
        self.assertEqual(find_distance_to_polygon((lat, lon)), 'Точка находится внутри МКАДа!')
