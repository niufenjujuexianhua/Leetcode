class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        0 1 2 3 4 5 6
        """
        cost.sort(reverse = True)
        i = 0
        res = 0
        for i in range(len(cost)):
            if i % 3 == 0 or i % 3 == 1:
                res += cost[i]
        return res 