class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, e = 1, n
        while s <= e:
            m = s + (e - s) // 2
            if isBadVersion(m):
                e = m - 1 
            else:
                s = m + 1 
        return s 