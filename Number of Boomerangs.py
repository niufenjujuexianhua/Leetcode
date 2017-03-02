class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for x1, y1 in points:
            dt = {}
            for x2, y2 in points:
                distance = (x1-x2)**2 + (y1-y2)**2
                dt[distance] = dt.get(distance, 0) + 1
            for i in dt:
                res += dt[i] * (dt[i]-1)

        return res

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        import collections
        total, disMat = 0, [[(i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 for j in points] for i in points]
        for i in range(len(points)):
            count = collections.Counter(disMat[i][:])
            for val in count.values():
                total += val * (val - 1)
        return total


if __name__ == '__main__':
    result = Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]])
    print(result)