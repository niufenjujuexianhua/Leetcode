class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        0 1 2 3 4 5 6
              x
        """
        if n == 1:
            return maxSum
        maxSum -= n
        s, e = 1, maxSum
        while s + 1 < e:
            m = s + (e - s) // 2
            if self.valid(m, index, n) <= maxSum:
                s = m
            else:
                e = m
        if self.valid(e, index, n):
            return e
        if self.valid(s, index, n):
            return s

    def valid(self, a, index, n):
        b = max(a - index, 0)
        res = (a + b) * (a - b + 1) / 2
        b = max(a - ((n - 1) - index), 0)
        res += (a + b) * (a - b + 1) / 2
        return res - a