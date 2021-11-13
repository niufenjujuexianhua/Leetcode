class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dfs(n, {})
    
    def dfs(self, n, dp):
        if n <= 1:
            return n 
        if n in dp:
            return dp[n]
        ans = self.dfs(n - 1, dp) + self.dfs(n - 2, dp)
        dp[n]= ans 
        return ans 