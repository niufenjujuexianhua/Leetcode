class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key = lambda x : x[1] - x[0])
        res = 0
        for a, m in tasks:
            res = max(res + a, m)
        return res