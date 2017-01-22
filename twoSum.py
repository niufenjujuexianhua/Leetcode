#==============================================================================
# Brute Force
# Issue log:
#     1. need to add i != k. see comment below
#     2. need to consider when len(nums) is less then 2
#==============================================================================

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        for i in range(len(nums)):
            for k in range(len(nums)):
                # need to add i != k. otherwise the output index for this case will be [0, 0]. [3,2,4,1] target=6
                if nums[i] + nums[k] == target and i != k:
                    return [i, k]


if __name__ == '__main__':
    result = Solution().twoSum([1, 9, -1, 0, -2, 2], 7)
    print(result)