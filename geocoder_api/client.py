from decimal import Decimal
from typing import Tuple

import requests

from .exceptions import InvalidKey, NothingFound, UnexpectedResponse


class Client:
    """Yandex geocoder API client.
    :Example:
        >>> from geocoder_api import Client
        >>> client = Client("your-api-key")
        >>> coordinates = client.transform_to_coordinates("Казань, ул. Чернышевского, 27")
        >>> assert transform_to_coordinates == (Decimal("55.790944"), Decimal("49.107752"))
        >>> address = client.address(Decimal("55.790944"), Decimal("49.107752"))
        >>> assert address == 'Россия, Республика Татарстан, Казань, улица Чернышевского, 27'
    """

    def __init__(self, api_key: str):
        self.api_key = api_key

    def _request(self, address: str) -> dict:
        response = requests.get(
            "https://geocode-maps.yandex.ru/1.x/",
            params=dict(format="json", apikey=self.api_key, geocode=address),
        )

        if response.status_code == 200:
            return response.json()["response"]
        elif response.status_code == 403:
            raise InvalidKey()
        else:
            raise UnexpectedResponse(
                f"status_code={response.status_code}, body={response.content}"
            )

    def transform_to_coordinates(self, address: str) -> Tuple[Decimal, ...]:
        """Fetch coordinates (longitude, latitude) for passed address."""
        data = self._request(address)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{address}" not found')

        coordinates = data[0]["GeoObject"]["Point"]["pos"]  # type: str
        longitude, latitude = tuple(coordinates.split(" "))

        return Decimal(latitude), Decimal(longitude)

    def address(self, latitude: Decimal, longitude: Decimal) -> str:
        """Fetch address for passed coordinates."""
        response = self._request(f"{longitude},{latitude}")
        data = response["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{latitude} {longitude}"')

        return data[0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]
