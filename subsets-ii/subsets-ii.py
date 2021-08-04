class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.bt(sorted(nums), 0, [], res)
        return res
    
    def bt(self, nums, i, path, res):
        res.append(path[:])

        seen = set()
        for j in range(i, len(nums)):
            if nums[j] in seen:
                continue
            seen.add(nums[j])
            self.bt(nums, j + 1, path + [nums[j]], res)