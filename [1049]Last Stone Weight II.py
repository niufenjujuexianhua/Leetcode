# You are given an array of integers stones where stones[i] is the weight of the
#  ith stone. 
# 
#  We are playing a game with the stones. On each turn, we choose any two stones
#  and smash them together. Suppose the stones have weights x and y with x <= y. T
# he result of this smash is: 
# 
#  
#  If x == y, both stones are destroyed, and 
#  If x != y, the stone of weight x is destroyed, and the stone of weight y has 
# new weight y - x. 
#  
# 
#  At the end of the game, there is at most one stone left. 
# 
#  Return the smallest possible weight of the left stone. If there are no stones
#  left, return 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0, so the array converts to [1], then that's the
#  optimal value.
#  
# 
#  Example 2: 
# 
#  
# Input: stones = [31,26,33,21,40]
# Output: 5
#  
# 
#  Example 3: 
# 
#  
# Input: stones = [1,2]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= stones.length <= 30 
#  1 <= stones[i] <= 100 
#  
#  Related Topics Dynamic Programming 
#  👍 1115 👎 44


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        return self.dfs(stones, 0, 0, {})

    def dfs(self, stones, i, total, memo):
        if (i, total) in memo:
            return memo[(i, total)]

        memo[(i, total)] = 0
        if i == len(stones):
            memo[(i, total)] = abs(sum(stones) - total * 2)
        else:
            memo[(i, total)] = min(self.dfs(stones, i + 1, total + stones[i], memo),
                                   self.dfs(stones, i + 1, total, memo))
        return memo[(i, total)]






        # target = sum(stones) // 2
        # dp = [0] * (target + 1)
        # # dp[0] = 1
        # res = 0
        # for stone in stones:
        #     for size in range(target, -1, -1):
        #         if size >= stone:
        #             dp[size] = max(dp[size], stone + dp[size - stone])
        # return sum(stones) - dp[-1] * 2

        # total = sum(stones)
        #
        # Max_weight = int(total / 2)
        #
        # current = (Max_weight + 1) * [0]
        #
        # for v in stones:
        #     for w in range(Max_weight, -1, -1):
        #         if w - v >= 0:
        #             current[w] = max(v + current[w - v], current[w])
        #
        # return total - 2 * current[-1]

# class Solution:
#     def lastStoneWeightII(self, stones):
#         s = sum(stones)
#         dp = [0] * (s // 2 + 1)
#         dp[0] = 1
#         for i in range(len(stones)):
#             for j in range(s // 2, -1, -1):
#                 if j - stones[i] < 0: break
#                 if dp[j - stones[i]]:
#                     dp[j] = 1
#
#         res = s + 1
#         for psum in range(1, s // 2):
#             if dp[psum] and 2 * psum - s >= 0:
#                 res = min(res, 2 * psum - s)
#         return res
# print(Solution().lastStoneWeightII([31,26,33,21,40]))
# print(Solution().lastStoneWeightII([2,7,4,1,8,1]))
# leetcode submit region end(Prohibit modification and deletion)
