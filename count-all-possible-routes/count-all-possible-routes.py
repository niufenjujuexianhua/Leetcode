class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        self.mod = 10 ** 9 + 7
        return self.dfs(locations, locations[start], locations[finish], fuel, {})

    def dfs(self, locations, s, e, f, dp):
        if f < 0:
            return 0
        if (s, f) in dp:
            return dp[(s, f)]

        ans = int(s == e)
        for nxt in locations:
            if nxt != s:
                ans += self.dfs(locations, nxt, e, f - abs(nxt - s), dp)
        ans %= self.mod
        dp[(s, f)] = ans
        return ans