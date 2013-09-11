from unittest import TestCase
from vtown import geo
from vtown.geo.polygon import Polygon
from nose.tools import *
    
class TestPolygon(TestCase):
                
    def test_distance(self):
        distance = geo.LatLon(42.39321,-82.92114).distance(geo.LatLon(42.39194,-82.91669))
        self.assertEquals(distance, 0.3915340284873347)