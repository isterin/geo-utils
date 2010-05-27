from unittest import TestCase
from vtown import geo
from nose.tools import *


def test_point():
    point = geo.Point(x=80,y=90)
    assert point.x == 80
    assert point.y == 90
    
def test_lat_lon():
    lat_lon = geo.LatLon(lat=80, lon=90)
    assert lat_lon.lat == 80
    assert lat_lon.lon == 90
    assert lat_lon.y == 80
    assert lat_lon.x == 90
    
    lat_lon = geo.LatLon.from_point(geo.Point(88,99))
    assert lat_lon.lat == 99
    assert lat_lon.lon == 88
    assert lat_lon.y == 99
    assert lat_lon.x == 88