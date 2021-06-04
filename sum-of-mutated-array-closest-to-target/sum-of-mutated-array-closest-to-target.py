class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        s, e = 0, max(arr)
        while s + 1 < e:
            m = s + (e - s) // 2
            total = self.check(arr, m)
            if total >= target:
                e = m
            else:
                s = m
        if abs(self.check(arr, e) - target) < abs(self.check(arr, s) - target):
            return e
        return s

    def check(self, arr, m):
        return sum([a if a <= m else m for a in arr])