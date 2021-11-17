class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        find the largest n s.t. n ** 2 <= x
        """
        s, e = 0, x 
        while s <= e:
            m = s + (e - s) // 2 
            # if m ** 2 == x:
            #     return m 
            if m ** 2 <= x:
                s = m + 1 
            else:
                e = m - 1 
        return e 