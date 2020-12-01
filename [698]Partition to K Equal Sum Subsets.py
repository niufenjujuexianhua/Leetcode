# Given an array of integers nums and a positive integer k, find whether it's po
# ssible to divide this array into k non-empty subsets whose sums are all equal. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,
# 3) with equal sums.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= k <= len(nums) <= 16. 
#  0 < nums[i] < 10000. 
#  
#  Related Topics Dynamic Programming Recursion 
#  👍 2384 👎 153


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums.sort(reverse = True)
        s = sum(nums)
        if s % k != 0:
            return False

        s //= k
        if nums[0] > s:
            return False

        return self.dfs(nums, s, s, k, set())

    def dfs(self, nums, cur, s, k, seen):
        if cur == 0:
            return self.dfs(nums, s, s, k - 1, seen)
        if len(seen) == len(nums):
            if k == 0:
                return True
            return False

        for j in range(len(nums)):
            if nums[j] > cur or j in seen:
                continue
            seen.add(j)
            if self.dfs(nums, cur - nums[j], s, k, seen):
                return True
            seen.remove(j)
        return False
print(Solution().canPartitionKSubsets([85,35,40,64,86,45,63,16,5364,110,5653,97,95],
7))
# leetcode submit region end(Prohibit modification and deletion)
