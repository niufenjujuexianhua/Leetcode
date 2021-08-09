class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = prices[0]
        res = 0
        for p in prices[1:]:
            res = max(res, p - lowest)
            lowest = min(lowest, p)
        return res 