class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s, e = 0, len(nums) - 1 
        while s <= e:
            m = s + (e - s) // 2
            if nums[m] == target:
                return m

            if nums[m] >= nums[s]:
                if nums[s] <= target <= nums[m]:
                    e = m - 1
                else:
                    s = m + 1
            else:
                if nums[e] >= target >= nums[m]:
                    s = m + 1
                else:
                    e = m - 1
        return -1