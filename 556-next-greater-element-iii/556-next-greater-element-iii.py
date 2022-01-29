class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return -1
        nums = list(str(n))
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            return -1

        for j in reversed(range(i + 1, len(nums))):
            if nums[j] > nums[i]:
                break

        nums[j],  nums[i] = nums[i], nums[j]
        nums[i + 1:] = sorted(nums[i + 1:])
        res = int(''.join(nums))
        return res if res <= 2 ** 31 - 1 else -1
        return 