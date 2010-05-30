"""
Polygon related utility classes/functions
"""
import numpy
from vtown.geo import private, Point, Line, BoundingBox

class Polygon(object):
    """Polygon class represents a set of points on a cartesian plane which form a polygon"""
    def __init__(self, *points):
        super(Polygon, self).__init__()
        self.points = list()
        for p in points:
            if isinstance(p, Point):
                self.points.append(p)
            elif isinstance(p, dict):
                self.points.append( 
                        Point(x=p.get('x', p['lon']), y=p.get('y', p['lat'])) )
            elif isinstance(p, (list, tuple)):
                self.points.append(Point(*p))
            else:
                raise TypeError("Points must be provided in a form of a Point class, dictionary, list, " \
                                "or tuple instances. You've provided %s instance." % p.__class__)
        if len(self.points) < 3 or self.points[0] != self.points[len(self.points)-1]:
            raise ValueError("The points you provided do not define a polygon.  " \
                             "The first and last points must be the same.")
    
    def contains(self, point):
        seg_counter = private.SegmentCounter(point)
        for i in range(1, len(self.points)):
            line = Line(*self.points[i-1:i+1])
            if seg_counter.process_segment(line):
                return True
        return seg_counter.crossings % 2 == 1
        
    def random_point(self):
        bb = BoundingBox(*self.points)
        while True:
            p = bb.random_point()
            if self.contains(p):
                return p