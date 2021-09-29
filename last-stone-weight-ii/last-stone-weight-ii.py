class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        ss = {0}
        for s in stones:
            ss |= {s + i for i in ss}

        total = sum(stones)
        return min(abs(total - s - s) for s in ss)