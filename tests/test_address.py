from decimal import Decimal
import unittest

from app.client import Client
from app.exceptions import NothingFound, InvalidKey
from config import api_key



class Test(unittest.TestCase):
    """Test cases to see if the address correctly converts to coordinates and vice versa.
    Also basic exceptions are tested"""

    def test_if_address_found(self):
        client = Client(api_key)
        self.assertEqual(client.transform_to_coordinates('Калининградская область, '
                                                         'пос. Малое Исаково, ул. Молодёжная, д.19Б'),
                         (Decimal('54.736758'), Decimal('20.586296')))

    def test_if_address_not_found(self):
        client = Client(api_key)
        self.assertRaises(NothingFound, client.transform_to_coordinates, 'фывафвыафы')

    def test_if_coordinates_found(self):
        client = Client(api_key)
        self.assertEqual(client.address(Decimal('54.736758'), Decimal('20.586296')),
                         'Россия, Калининградская область, '
                         'Гурьевский муниципальный округ, '
                         'посёлок Малое Исаково, Молодёжная улица, 19Б')

    def test_if_coordinates_not_found(self):
        client = Client(api_key)
        self.assertRaises(NothingFound, client.address, Decimal('540'), Decimal('540'))

    def test_if_apikey_nonexistent(self):
        client = Client('some_non_existing_key')
        self.assertRaises(InvalidKey, client.transform_to_coordinates, 'Красная площадь')


if __name__ == '__main__':
    unittest.main()
