class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)


class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums)+1)) - sum(nums)
if __name__ == '__main__':
    result = Solution2().missingNumber([0, 1, 3])
    print(result)