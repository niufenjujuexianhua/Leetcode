class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        s, e = 1, position[-1] - position[0]
        while s + 1 < e:
            mid = s + (e - s) // 2
            if self.valid(position, mid, m):
                s = mid
            else:
                e = mid
        if self.valid(position, e, m):
            return e
        if self.valid(position, s, m):
            return s

    def valid(self, position, mid, m):
        prev = 0
        for i, p in enumerate(position):
            if i == 0:
                m -= 1
            elif p - position[prev] >= mid:
                m -= 1
                prev = i 

            if m == 0:
                break
        return m <= 0