class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        res = [float('inf')]
        for base in baseCosts:
            self.dfs(target, toppingCosts, 0, res, base)
        return res[0]


    def dfs(self, target, toppingCosts, i, res, total):
        if abs(total - target) == abs(res[0] - target):
            res[0] = min(res[0], total)
            return

        if abs(total - target) < abs(res[0] - target):
            res[0] = total

        if i >= len(toppingCosts) or total > target:
            return

        for j in range(i, len(toppingCosts)):
            for cnt in range(3):
                self.dfs(target, toppingCosts, j + 1, res, total + cnt * toppingCosts[j])