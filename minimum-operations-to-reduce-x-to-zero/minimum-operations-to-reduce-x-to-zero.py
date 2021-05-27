class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        need = sum(nums) - x
        dt, res, total = {0 : -1}, float('-inf'), 0
        for i, n in enumerate(nums):
            total += n
            dt[total] = i
            if total - need in dt:
                res = max(res, i - dt[total - need])

        return len(nums) - res if res != float('-inf') else -1