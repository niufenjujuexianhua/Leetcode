class Solution(object):
    def maxHeight(self, A):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        A = [[0, 0, 0]] + sorted(map(sorted, A))
        dp = [0] * len(A)
        for j in xrange(1, len(A)):
            for i in xrange(j):
                if all(A[i][k] <= A[j][k] for k in xrange(3)):
                    dp[j] = max(dp[j], dp[i] + A[j][2])
        return max(dp)