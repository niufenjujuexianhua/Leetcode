class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums

        lt, rt = self.sortArray(nums[: n//2]), self.sortArray(nums[n//2 :])

        i = j = k = 0
        while i < len(lt) and j < len(rt):
            if lt[i] <= rt[j]:
                nums[k] = lt[i]
                i += 1
            else:
                nums[k] = rt[j]
                j += 1
            k += 1

        while i < len(lt):
            nums[k] = lt[i]
            i += 1
            k += 1 
        while j < len(rt):
            nums[k] = rt[j]
            j += 1
            k += 1
        return nums 