class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        n = len(stations)
        dp = [startFuel] + [0] * n
        for i, (dis, cap) in enumerate(stations):
            for t in reversed(range(i + 1)):
                if dp[t] >= dis:
                    dp[t + 1] = max(dp[t + 1], dp[t] + cap)

        for i, d in enumerate(dp):
            if d >= target:
                return i
        return -1 