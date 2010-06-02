Currently there are two helpful utility functions here.

1.  [Point-in-polygon](http://en.wikipedia.org/wiki/Point_in_polygon) test
2.  Random point generator.  Right now it performs better if the polygon
    covers a large portion of its bounding box.  The test is performed using
    this algorithm.
    
    1.  Generate a [bounding box](http://en.wikipedia.org/wiki/Minimum_bounding_rectangle)
    2.  Generate a random point within this bounding box
    3.  Perform a point-in-polygon test on this point.  If the test succeeds, return the point,
        if not loop to step a and perform again.
        
    \*\* If anyone know of a better way to do above, let me know.  I'd love to hear some better ideas
    especially when dealing with complex concave polygons.
    

USAGE:
  
  Point-in-polygon test:
  
  <pre>
  polygon = Polygon((0,0), (0,4), (4,4), (4,0), (0,0))
  point = geo.Point(2,2)
  assert polygon.contains(geo.Point(2,2))
  </pre>
  
  Random point within a polygon
  
  <pre>
  polygon = Polygon(  geo.LatLon(42.39321,-82.92114),
                        geo.LatLon(42.39194,-82.91669),
                        geo.LatLon(42.39147,-82.91796),
                        geo.LatLon(42.39090,-82.91974),
                        geo.LatLon(42.39321,-82.92114))

  point = polygon.random_point()
  assert polygon.contains(point)
  </pre>
  
  
INSTALLATION:
  You can install the package either by cloning this repository and running the standard
  
    python setup.py install
    
  or install from pypi
  
    pip install geo-utils