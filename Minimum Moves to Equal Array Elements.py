class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = min(nums)
        return sum([i-minimum for i in nums])

class Solution2(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = min(nums)
        return sum(nums) - len(nums)*minimum



if __name__ == '__main__':
    result = Solution().minMoves([1,2,3])
    print(result)