class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) == 1:
            return 0
        s, e = 0, len(nums) - 1
        while s + 1 < e:
            m = s + (e - s) // 2
            if nums[m] > nums[m + 1]:
                e = m
            else:
                s = m

        if nums[s] > nums[e]:
            return s
        return e
        
# leetcode submit region end(Prohibit modification and deletion)
