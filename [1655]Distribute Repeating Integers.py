# You are given an array of n integers, nums, where there are at most 50 unique 
# values in the array. You are also given an array of m customer order quantities,
#  quantity, where quantity[i] is the amount of integers the ith customer ordered.
#  Determine if it is possible to distribute nums such that: 
# 
#  
#  The ith customer gets exactly quantity[i] integers, 
#  The integers the ith customer gets are all equal, and 
#  Every customer is satisfied. 
#  
# 
#  Return true if it is possible to distribute nums according to the above condi
# tions. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,4], quantity = [2]
# Output: false
# Explanation: The 0th customer cannot be given two different integers.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,3], quantity = [2]
# Output: true
# Explanation: The 0th customer is given [3,3]. The integers [1,2] are not used.
# 
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,1,2,2], quantity = [2,2]
# Output: true
# Explanation: The 0th customer is given [1,1], and the 1st customer is given [2
# ,2].
#  
# 
#  Example 4: 
# 
#  
# Input: nums = [1,1,2,3], quantity = [2,2]
# Output: false
# Explanation: Although the 0th customer could be given [1,1], the 1st customer 
# cannot be satisfied. 
# 
#  Example 5: 
# 
#  
# Input: nums = [1,1,1,1,1], quantity = [2,3]
# Output: true
# Explanation: The 0th customer is given [1,1], and the 1st customer is given [1
# ,1,1].
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 105 
#  1 <= nums[i] <= 1000 
#  m == quantity.length 
#  1 <= m <= 10 
#  1 <= quantity[i] <= 105 
#  There are at most 50 unique values in nums. 
#  Related Topics Dynamic Programming Backtracking 
#  👍 34 👎 1


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution(object):
    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quntantity: List[int]
        :rtype: bool
        """
        freq = collections.Counter(nums)
        freq = list(map(list, freq.items()))
        # freq = sorted(map(list, freq.items()), key = lambda x : x[1], reverse = True)
        n = len(quantity)
        quantity.sort(reverse = True)
        return self.bt(0, quantity, freq, n)


    def bt(self, i, quantity, freq, n):
        if i == n:
            return True

        for j, (k, v) in enumerate(freq):
            # print(i, n)
            if v >= quantity[i]:
                freq[j][1] -= quantity[i]
                if self.bt(i + 1, quantity, freq, n):
                    return True
                freq[j][1] += quantity[i]
        return False






        # N = 1 << n
        # dp = [[False] * N for _ in range(len(freq) + 1)]
        # for i in range(len(freq) + 1):
        #     dp[i][0] = True
        #
        # for i, f in enumerate(freq.keys(), start = 1):
        #     for state in range(1, N):
        #         if dp[i - 1][state]:
        #             dp[i][state] = True
        #             continue
        #
        #         subset = state
        #         while subset:
        #             # print(subset)
        #             if not dp[i - 1][state ^ subset]:
        #                 # subset = (subset - 1) & state
        #                 continue
        #
        #             cnt = 0
        #             for j in range(len(bin(subset)[2:])):
        #                 # print(n, i)
        #                 if (subset >> (n - j - 1)) & 1 == 1:
        #                     cnt += quantity[j]
        #             if cnt <= freq[f]:
        #                 dp[i][state] = True
        #                 break
        #
        #             subset = (subset - 1) & state
        # return dp[-1][-1]

# print(Solution().canDistribute([1,1,2,3], [2,2]))
# leetcode submit region end(Prohibit modification and deletion)
