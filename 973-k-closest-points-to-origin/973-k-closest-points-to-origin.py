class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if K == len(points): return points 
        s, e = 0, len(points) - 1
        while s <= e:
            pos = self.partition(points, s, e)
            if pos + 1 == K:
                return points[:K]
            elif pos + 1 < K:
                s = pos + 1  
            else:
                e = pos - 1
        return

    def partition(self, points, s, e):
        # if s < e:
        import random
        p = random.randint(s, e)
        self.swap(points, p, e)
        pos = s - 1
        for i in range(s, e):
            if self.distance(points[i]) <= self.distance(points[e]):
                pos += 1
                self.swap(points, pos, i)
        pos += 1
        self.swap(points, pos, e)
        return pos


    def distance(self, point):
        return point[0] ** 2 + point[1] ** 2

    def swap(self, points, i, j):
        points[i], points[j] = points[j], points[i]