from decimal import Decimal
from flask import Blueprint, request, current_app
from shapely.geometry import Point
from main.distance_calculator import mkad, find_distance_to_polygon
from configs.config import api_key
from geocoder_api import Client
import logging

main = Blueprint('main', __name__)

log = logging.getLogger('werkzeug')
log.disabled = True
logging.basicConfig(filename='.log', level='INFO', format='%(message)s')


@main.route('/', methods=['GET'])
@main.route('/address', methods=['GET'])
def enter_address():
    address = request.args.get('address')
    client = Client(api_key)
    coordinates = client.transform_to_coordinates(address)
    if mkad.contains(Point(coordinates)):
        current_app.logger.info(f'{address} находится внутри МКАДа')
        return '''Точка находится внутри МКАДа!'''
    else:
        distance = find_distance_to_polygon(coordinates, mkad)
        current_app.logger.info(f'Расстояние от точки "{address}" до МКАДа составляет {distance} км')
        return f'Расстояние от точки: "{address}" до МКАДа составляет {distance} км'


@main.route('/coords', methods=['GET'])
def enter_coordinates():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    coordinates = Decimal(lat), Decimal(lon)
    if mkad.contains(Point(coordinates)):
        current_app.logger.info(f'Точка {lat, lon} находится внутри МКАДа')
        return '''Точка находится внутри МКАДа!'''
    else:
        distance = find_distance_to_polygon(coordinates, mkad)
        current_app.logger.info(f'Расстояние от точек: {lat, lon} до МКАДа составляет {distance} км')
        return f'Расстояние от точек {lat, lon} до МКАДа составляет {distance} км'

