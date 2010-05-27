"""
Geospatial utility classes/functions
"""

class Point(object):
    """Point class represents a point on a cartesian plane"""
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    def __hash__(self):
        """docstring for __hash__"""
        return self.x.hash() + self.y.hash()
    
    def __eq__(self, other):
        """docstring for __eq__"""
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        """docstring for __ne__"""
        return not self.__eq__(other)
    
    def __str__(self):
        return  "%s (x=%f, y=%f)" % (self.__class__.__name__, self.x, self.y)

class LatLon(Point):
    """docstring for LatLon"""
    def __init__(self, lat, lon):
        super(LatLon, self).__init__(x=lon, y=lat)
    
    @staticmethod
    def from_point(point):
        """docstring for from_point"""
        if not isinstance(point, Point):
            raise TypeError("You must provide a argument which is an instance of class Point.")
        return LatLon(lat=point.y, lon=point.x)
    
    @property
    def lat(self):
        return self.y
    
    @lat.setter
    def lat(self, val):
        self.y = val
    
    @property
    def lon(self):
        return self.x
    
    @lon.setter
    def lon(self, val):
        self.x = val
    
    def __str__(self):
        return  "%s (lat=%f, lon=%f)" % (self.__class__.__name__, self.lat, self.lon)

class Line(object):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def is_on_point(self, point):
        p, p1, p2 = point, self.point1, self.point2
        if p.x == p2.x and p.y == p2.y:
            return True
        
        if p1.y == p.y and p2.y == p.y:
            minx = p1.x
            maxx = p2.x
            if minx > maxx:
                minx = p2.x
                maxx = p1.x
            if p.x >= minx and p.x <= maxx:
                return True
        
        return False
