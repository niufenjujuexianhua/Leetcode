class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        cnt = [1] * n
        cnt[0] = cnt[1] = 0
        for i in range(2, n):
            if cnt[i] == 1:
                j = i
                while i * j < n:
                    cnt[i * j] = 0
                    j += 1
        return sum(cnt)