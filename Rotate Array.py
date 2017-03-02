class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        return nums[-k:] + nums[:-k]


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1

if __name__ == '__main__':
    result = Solution().rotate([1,2],1)
    print(result)