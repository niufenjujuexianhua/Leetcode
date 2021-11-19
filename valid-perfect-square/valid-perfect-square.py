class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s, e = 1, num
        while s <= e:
            m = s + (e - s) // 2
            if m * m == num:
                return True
            elif m * m < num:
                s = m + 1 
            else:
                e = m - 1 
        return False