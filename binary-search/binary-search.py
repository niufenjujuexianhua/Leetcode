class Solution(object):
    def search(self, nums, x):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s, e = 0, len(nums) - 1
        while s < e:
            m = s + (e - s) // 2
            # if m - 1 >= 0 or nums[m] < nums[m - 1]:
            #     return nums[m]

            if nums[m] < x:
                s = m + 1
            else:
                e = m
        if x == nums[s]:
            return s 
        return -1