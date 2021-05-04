class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n, cnt = len(nums), 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                cnt += 1
                if i == 1 or nums[i - 2] <= nums[i]: nums[i - 1] = nums[i]
                else: nums[i] = nums[i - 1]

        return cnt <= 1