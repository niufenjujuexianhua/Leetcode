class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sz = len(nums)
        idx, pivot = None, float('inf')

        for i, n in enumerate(nums):
            if abs(n) < pivot:
                idx, pivot = i, abs(n)

        i, j = idx - 1, idx + 1
        res = [nums[idx] ** 2]
        while i >= 0 and j < sz:
            if abs(nums[i]) <= abs(nums[j]):
                res.append(nums[i] ** 2)
                i -= 1
            else:
                res.append(nums[j] ** 2)
                j += 1

        while i >= 0:
            res.append(nums[i] ** 2)
            i -= 1

        while j < sz:
            res.append(nums[j] ** 2)
            j += 1

        return res