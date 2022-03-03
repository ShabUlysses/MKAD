import logging
from decimal import Decimal

from flask import Blueprint, request, current_app
from shapely.geometry import Point

from config import api_key
from .geocoder import Client
from .distance_calculator import mkad, find_distance_to_polygon

main = Blueprint('app', __name__)  # Create the blueprint of application

log = logging.getLogger('werkzeug')
log.disabled = True  # Setting the logging to save only results of http query
logging.basicConfig(filename='../.log', level='INFO', format='%(message)s')


@main.route('/')
def welcome_page():
    return '''С помощью данного приложения возможно рассчитать прямое расстояние от заданной точки до МКАД.'''


@main.route('/address', methods=['GET'])
def enter_address():
    """This function accepts http-query in form of address from user and returns the distance to MKAD.
    If given address is inside MKAD, then it return associated message."""
    address = request.args.get('address')
    client = Client(api_key)  # Connect to yandex-geocoder
    coordinates = client.transform_to_coordinates(address)

    if mkad.contains(Point(coordinates)): # Check if coordinates are inside MKAD
        current_app.logger.info(f'{address} находится внутри МКАДа')
        return '''Точка находится внутри МКАДа!'''
    else:
        distance = find_distance_to_polygon(coordinates, mkad)  # Calculate the distance
        current_app.logger.info(f'Расстояние от точки "{address}" до МКАДа составляет {distance} км')
        return f'Расстояние от точки: "{address}" до МКАДа составляет {distance} км'


@main.route('/coords', methods=['GET'])
def enter_coordinates():
    """This function accepts http-query in form of coordinates from user and returns the distance to MKAD.
    If given coordinates are inside MKAD, then it return associated message."""
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    coordinates = Decimal(lat), Decimal(lon)

    if mkad.contains(Point(coordinates)):  # Check if coordinates are inside MKAD
        current_app.logger.info(f'Точка {lat, lon} находится внутри МКАДа')
        return '''Точка находится внутри МКАДа!'''
    else:
        distance = find_distance_to_polygon(coordinates, mkad)  # Calculate the distance
        current_app.logger.info(f'Расстояние от точек: {lat, lon} до МКАДа составляет {distance} км')
        return f'Расстояние от точек {lat, lon} до МКАДа составляет {distance} км'
