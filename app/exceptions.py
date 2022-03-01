class YandexGeocoderException(Exception):
    """Class of exceptions for Yandex-Geocoder API"""
    pass


class UnexpectedResponse(YandexGeocoderException):
    """Raise exception if server returned unexpected response"""
    pass


class NothingFound(YandexGeocoderException):
    """Raise exception if no match for http query has been found"""
    pass


class InvalidKey(YandexGeocoderException):
    """Raise exception if Invalid key has been passed as api_key"""
    pass

