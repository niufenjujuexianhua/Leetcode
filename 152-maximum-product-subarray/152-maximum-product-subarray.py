class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp = [nums[0]]
        res = nums[0]
        mn = mx = nums[0]

        for n in nums[1:]:
            cur = max(n, mn * n, mx * n)
            res = max(res, cur)

            mn = min(n, mn * n, mx * n)
            mx = cur 
        return res