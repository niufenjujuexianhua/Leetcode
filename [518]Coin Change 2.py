# You are given coins of different denominations and a total amount of money. Wr
# ite a function to compute the number of combinations that make up that amount. Y
# ou may assume that you have infinite number of each kind of coin. 
# 
#  
#  
# 
#  
# 
#  Example 1: 
# 
#  
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#  
# 
#  Example 2: 
# 
#  
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#  
# 
#  Example 3: 
# 
#  
# Input: amount = 10, coins = [10] 
# Output: 1
#  
# 
#  
# 
#  Note: 
# 
#  You can assume that 
# 
#  
#  0 <= amount <= 5000 
#  1 <= coin <= 5000 
#  the number of coins is less than 500 
#  the answer is guaranteed to fit into signed 32-bit integer 
#  
#  👍 2832 👎 73


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        ans = self.dfs(0, amount, coins, {})
        return ans

    def dfs(self, i, rem, coins, memo):
        if rem == 0:
            return 1
        if rem < 0 or i == len(coins):
            return 0
        if (i, rem) in memo:
            return memo[(i, rem)]

        memo[(i, rem)] = 0
        memo[(i, rem)] += self.dfs(i, rem - coins[i], coins, memo) + self.dfs(i + 1, rem, coins, memo)
        return memo[(i, rem)]
        
# leetcode submit region end(Prohibit modification and deletion)
