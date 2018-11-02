class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
        self.d = 0
    def calDis(self):
        self.d = (self.x)**2 + (self.y)**2
    def __cmp__(self, other):
        p1xd = abs(self.x)
        p1yd = abs(self.y)
        p2xd = abs(other.x)
        p2yd = abs(other.y)
        p1d = p1xd**2 + p1yd**2  
        p2d = p2xd**2 + p2yd**2
        if p1d != p2d:
            return cmp(p1d, p2d)
        else:
            if p1xd != p2xd: 
                return cmp(p1xd, p2xd)
            else:
                return cmp(p1yd, p2yd)


class Solution(object):
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        n = len(points)
        if n < k: return []
        self.org = origin
        res = []
        for i, x in enumerate(points):
            res.append(x)
            self.heapify(res, len(res)-1 )
            if i >= k: 
                res.pop()
        return res
        
    def heapify(self, res, i):
        return
        

nums = [Point(1,2), Point(1,3), Point(2,1), Point(5,1), Point(6,1), Point(7,1), Point(8,1)] 

