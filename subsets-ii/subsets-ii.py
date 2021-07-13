class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums), 0, res, [])
        return res
        
    def dfs(self, nums, i, res, path):
        res.append(path)

        for j in range(i, len(nums)):
            if j > i and nums[j - 1] == nums[j]:
                continue
            self.dfs(nums, j + 1, res, path + [nums[j]])