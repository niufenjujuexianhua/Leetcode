class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        memo = {}

        def f(i, j):
            if i + 1 >= j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            min_cost = float('inf')
            for k in range(i + 1, j):
                cost = f(i, k) + f(k, j) + (cuts[j] - cuts[i])
                min_cost = min(min_cost, cost)
            memo[(i, j)] = min_cost
            return memo[(i, j)]

        cuts.sort()
        cuts = [0] + cuts + [n]
        return f(0, len(cuts) - 1)