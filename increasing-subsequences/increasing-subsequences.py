class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, i, res, path):
        if len(path) >= 2:
            res.append(path[:])

        seen = set()
        for j in range(i, len(nums)):
            if path and path[-1] > nums[j] or nums[j] in seen:
                continue
            seen.add(nums[j])
            self.dfs(nums, j + 1, res, path + [nums[j]])