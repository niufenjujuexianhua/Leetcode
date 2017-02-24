class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1):
            nums[i+1] ^= nums[i]
        return nums[i+1]


class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums)) - sum(nums)

class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import functools
        return functools.reduce((lambda x,y : x^y), nums)

if __name__ == '__main__':
    result = Solution3().singleNumber([1,1,4,5,6,4,5,7,7])
    print(result)