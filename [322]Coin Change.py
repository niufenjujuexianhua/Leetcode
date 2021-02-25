# You are given coins of different denominations and a total amount of money amo
# unt. Write a function to compute the fewest number of coins that you need to mak
# e up that amount. If that amount of money cannot be made up by any combination o
# f the coins, return -1. 
# 
#  You may assume that you have an infinite number of each kind of coin. 
# 
#  
#  Example 1: 
# 
#  
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#  
# 
#  Example 2: 
# 
#  
# Input: coins = [2], amount = 3
# Output: -1
#  
# 
#  Example 3: 
# 
#  
# Input: coins = [1], amount = 0
# Output: 0
#  
# 
#  Example 4: 
# 
#  
# Input: coins = [1], amount = 1
# Output: 1
#  
# 
#  Example 5: 
# 
#  
# Input: coins = [1], amount = 2
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 231 - 1 
#  0 <= amount <= 104 
#  
#  Related Topics Dynamic Programming 
#  👍 6099 👎 183


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans = self.dfs(amount, sorted(coins), {})
        return ans if ans != float('inf') else -1

    def dfs(self, rem, coins, memo):
        if rem == 0:
            return 0
        if rem in memo:
            return memo[rem]

        memo[rem] = float('inf')
        for c in coins:
            if c > rem:
                break
            memo[rem] = min(memo[rem],
                            self.dfs(rem - c, coins, memo) + 1)
        return memo[rem]



# leetcode submit region end(Prohibit modification and deletion)
