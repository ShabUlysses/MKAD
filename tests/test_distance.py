import unittest
from decimal import Decimal

from shapely.geometry import Point

from config import api_key
from app.client import Client
from app.distance_calculator import find_distance_to_polygon, mkad


class Test(unittest.TestCase):
    def test_find_distance_with_address(self):
        client = Client(api_key)
        coordinates = client.transform_to_coordinates('Можайск')
        self.assertEqual(find_distance_to_polygon(coordinates), 88)

    def test_find_distance_with_coordinates(self):
        lat, lon = Decimal(54.719362), Decimal(20.505681)
        self.assertEqual(find_distance_to_polygon((lat, lon)), 1072)

    def test_address_inside_mkad(self):
        client = Client(api_key)
        coordinates = client.transform_to_coordinates('Красная площадь')
        self.assertEqual(mkad.contains(Point(coordinates)), True) # True if point is inside MKAD

    def test_coordinates_inside_mkad(self):
        lat, lon = Decimal(55.778892), Decimal(37.59542)
        self.assertEqual(mkad.contains(Point((lat, lon))), True) # True if point is inside MKAD


if __name__ == '__main__':
    unittest.main()
