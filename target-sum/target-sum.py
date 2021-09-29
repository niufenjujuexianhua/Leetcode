class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        seen = {}
        return self.dfs(nums, 0, target, seen, 0)

    def dfs(self, nums, i, target, seen, cur):
        if (i, cur) in seen:
            return seen[(i, cur)]
        if i == len(nums):
            return int(cur == target)

        neg = self.dfs(nums, i + 1, target, seen, cur - nums[i])
        pos = self.dfs(nums, i + 1, target, seen, cur + nums[i])

        seen[(i, cur)] = neg + pos
        return seen[(i, cur)]