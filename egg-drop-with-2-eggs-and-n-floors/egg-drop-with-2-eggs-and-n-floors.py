class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dfs(n, 2, {})

    def dfs(self, floors, eggs, dp):
        if floors == 1 or eggs == 1:
            return floors
        if (floors, eggs) in dp:
            return dp[(floors, eggs)]
        
        ans = float('inf')
        for f in range(1, floors + 1):
            ans = min(ans, 
                      1 + max(self.dfs(f - 1, eggs - 1, dp), self.dfs(floors - f, eggs, dp)))
        dp[(floors, eggs)] = ans 
        return ans 