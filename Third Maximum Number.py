class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) < 3:
            return max(nums)
        return nums[2]


class Solution2(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)

        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')

        for i in nums:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i

        return max3

class Solution3(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)

        heapq.heapify(nums)

        return min(heapq.nlargest(3, nums))

if __name__ == '__main__':
    result = Solution2().thirdMax([2, 2, 3, 1])
    print(result)