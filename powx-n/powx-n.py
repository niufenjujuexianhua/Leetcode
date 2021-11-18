class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1.0 / x
        res = 1

        while n:
            if n % 2 == 1:
                res *= x
                # n -= 1
            # else:
            x *= x
            n //= 2

        # res *= x
        return res