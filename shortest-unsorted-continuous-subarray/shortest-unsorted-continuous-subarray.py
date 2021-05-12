class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        minn, maxn = float('inf'), float('-inf')
        i, j = 1, len(nums) - 2

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                minn = min(minn, nums[i])

        for j in range(len(nums) - 2, -1, -1):
            if nums[j] > nums[j + 1]:
                maxn = max(maxn, nums[j])

        for i in range(len(nums)):
            if nums[i] > minn:
                lt = i
                break
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] < maxn:
                rt = j
                break

        return j - i + 1 if j > i else 0 