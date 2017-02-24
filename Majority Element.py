class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]

        return sorted(nums)[len(nums)/2]


if __name__ == '__main__':
    result = Solution().majorityElement([3,3,4])
    print(result)