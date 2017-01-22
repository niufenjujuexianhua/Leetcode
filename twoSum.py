'''
Brute Force
    Issue log:
        1. need to add i != k. see comment below
        2. need to consider when len(nums) is less then 2

using dictionary
'''

#Brute Force  time O(n^2)
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

#using dictionary only one for loop  O(n)
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
            
        dict = {}
        for idx, value in enumerate(nums):
#        for idx in range(len(nums)):
            if (target - value) in dict:
                return [dict[target-value], idx]
            else:
                dict[nums[idx]] = idx
        
        

if __name__ == '__main__':
    result = Solution2().twoSum([1, 9, -1, 0, -2, 2], 7)
    print(result)