import numpy

def det_2x2(mat):
  return float(mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0])

class SegmentCounter(object):
    
    def __init__(self, point):
        self.point = point
        self.crossings = 0
    
    def process_segment(self, line):
        p, p1, p2 = self.point, line.point1, line.point2
        if p1.x < p.x and p2.x < p.x:
            return False
        
        if (p.x == p2.x and p.y == p2.y):
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
        
        
        if ((p1.y > p.y) and (p2.y <= p.y)) \
                or ((p2.y > p.y) and (p1.y <= p.y)):
            x1 = p1.x - p.x
            y1 = p1.y - p.y
            x2 = p2.x - p.x
            y2 = p2.y - p.y

            det = 0
            ## det function fails on certain architectures with index out of bounds
            ## below we try it and it it fails, reserve to a 2x2 easy determinant calculation
            try:  
                det = numpy.linalg.det([[x1, y1], [x2, y2]])
            except:
                det = det_2x2([[x1, y1], [x2, y2]])
            
            if det == 0.0:
                return True
            if y2 < y1:
                det = -det
            
            if det > 0.0:
                self.crossings += 1