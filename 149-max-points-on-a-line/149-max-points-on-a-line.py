class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        import collections
        res = 0

        for i in range(len(points) - 1):
            overlap = 0
            dt = collections.defaultdict(int)

            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                if p1 == p2:
                    overlap += 1
                    continue

                key = self.gcd(p1, p2)
                dt[key] += 1

            res = max(res, max(dt.values()))
        return res + 1


    def gcd(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        if y1 == y2:
            return (x1, 0)
        if x1 == x2:
            return (0, y1)

        s1, s2 = y1 - y2, x1 - x2
        # if s1 < 0:
        #     s1, s2 = -s1, -s2

        d = self._gcd(s1, s2)
        return (s1 // d, s2 // d)

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

# print(Solution().maxPoints([[0,0],[2,2],[-1,-1]]))
# print(Solution().maxPoints([[9,-25],[-4,1],[-1,5],[-7,7]]))
