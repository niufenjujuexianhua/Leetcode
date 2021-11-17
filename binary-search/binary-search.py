class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s, e = 0, len(nums) - 1
        ans = -1
        while s <= e:
            m = s + ( e - s) // 2
            if nums[m] == target:
                ans = m 
                break
            elif nums[m] < target:
                s = m + 1 
            else:
                e = m - 1 
        
        return ans 