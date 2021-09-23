class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in reversed(range(n)):
            for j in range(i, n):
                if s[i] == s[j]:
                    if i + 1 <= j - 1:
                        dp[i][j] = dp[i + 1][j - 1]
                    else:
                        dp[i][j] = True
                # else:
                #     dp[i][j] = False

        for i in range(1, n - 1):
            for j in range(i, n - 1):
                if dp[0][i - 1] and dp[i][j] and dp[j + 1][n - 1]:
                    return True
        return False