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
    
    polygon = Polygon(  geo.LatLon(42.39321,-82.92114),
                        geo.LatLon(42.39194,-82.91669),
                        geo.LatLon(42.39147,-82.91796),
                        geo.LatLon(42.39090,-82.91974),
                        geo.LatLon(42.39321,-82.92114))
                        
    point = polygon.random_point()
    print("POINT: %s" % point)
    assert polygon.contains(point)
    
def test_bounding_box_in_relation_to_polygon():
    polygon = Polygon(  geo.LatLon(42.39321,-82.92114),
                        geo.LatLon(42.39194,-82.91669),
                        geo.LatLon(42.39147,-82.91796),
                        geo.LatLon(42.39090,-82.91974),
                        geo.LatLon(42.39321,-82.92114))
    bb = geo.BoundingBox(*polygon.points)
    for idx in range(0, 1000):
        p = bb.random_point()
        if not polygon.contains(p):
            print("Generated a point outside of polygon in %s tries. (%s)" % (idx, p))
            break
    else:
        raise AssertionError("Couldn't generate an out of polygon point within a bounding box.  " \
                             "This doesn't necessarily mean that the code is broken, since it's based on " \
                             "randomness.  Try to rerun the test or increase the amount of tries.")