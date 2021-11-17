class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, e = 1, n
        while s <= e:
            m = s + (e - s) // 2
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                e = m - 1
            else:
                s = m + 1
        return