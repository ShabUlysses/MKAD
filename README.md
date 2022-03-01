## Description

This application allows you to calculate the direct distance from inputed location to the MKAD (Moscow Ring Road). Application uses [Yandex-Geocoder API ](https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/about.html). Location can be inputed as address or as coordinates.

## Installation

First, clone this repository.

```
$ git clone http://github.com/ShabUlysses/MKAD
```

```
$ cd MKAD
```

Then, install plugins and packages that are necessary for this project to run:

```
$ pip install -r requirements.txt
```

Yandex Geocoder requires an API developer key, you can get it [here](https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/about.html) to use this library.
Create .env file in root directory of the project. Inside .env file create variable "api_key" and assign your API_KEY to it

```
Example:
api_key = 'your_api_key_here'
```

Then, run the application:

```
$ python run.py
```

To see application, access this url in your browser:
http://localhost:5000

You should see the welcome page if everything has been done correctly.

## Usage example

If the inputed locations is inside MKAD, then the application will return the associated message. If the location is outside MKAD, the location will return the distance in km from location to MKAD.
The application allows to enter both coordinates and address. Below are examples of writing https for address and for coordinates.
To enter address:
```
Example:
localhost:5000/address?addres=Калининград, ул. Генерала Озерова, д.7
```

To enter coordinates:
You need to enter latitude and longitude in GET request
```
Example:
http://localhost:5000/coords?lat=50&lon=50
```

## Tests

To run tests:
```
$ python -m unittest
```

## Docker

To create docker-image:
```
$ docker build -t <name:tag> .
```

To run a container:
```
$ docker run -d -p 5000:5000 <image_name>
```



