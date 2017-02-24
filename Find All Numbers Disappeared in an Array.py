class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            x = abs(nums[i])
            nums[x-1] = -abs(nums[x-1])
        return [i + 1 for i, k in enumerate(nums) if k > 0]


class Solution2(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        for i in range(len(nums)):
            pos = nums[i] - 1
            nums[pos] = nums[pos] + N
        return [i + 1 for i, v in enumerate(nums) if v <= N]

if __name__ == '__main__':
    result = Solution2().findDisappearedNumbers([1,1,2,2])
    print(result)