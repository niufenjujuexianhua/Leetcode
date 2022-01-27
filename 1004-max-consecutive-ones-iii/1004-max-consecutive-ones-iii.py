class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        zeros = 0
        res = 0
        for j, n in enumerate(nums):
            if n == 0:
                zeros += 1

            while zeros > k:
                if nums[i] == 0:
                    zeros -= 1
                i += 1

            res = max(res, j - i + 1)
        return res