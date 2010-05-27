from unittest import TestCase
from vtown import geo
from vtown.geo.polygon import Polygon
from nose.tools import *
    
def test_polygon():
    polygon = Polygon((99,88), {'lat': 85, 'lon': 95}, geo.Point(98, 89), geo.LatLon(87, 78), (99,88))
    assert len(polygon.points) == 5
    
@raises(ValueError)
def test_invalid_polygon():
    polygon = Polygon((99,88), {'lat': 85, 'lon': 95}, geo.Point(98, 89), geo.LatLon(87, 78))
    
    
def test_point_in_polygon():
    polygon = Polygon((0,0), (0,4), (4,4), (4,0), (0,0))
    point = geo.Point(2,2)
    assert polygon.contains(geo.Point(2,2))
    assert not polygon.contains(geo.Point(5,5))
    
def test_generate_random_point_in_polygon():
    polygon = Polygon((0,0), (0,4), (4,4), (4,0), (0,0))
    point = polygon.random_point()
    print("POINT: %s" % point)
    assert polygon.contains(point)