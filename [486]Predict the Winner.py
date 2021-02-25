# Given an array of scores that are non-negative integers. Player 1 picks one of
#  the numbers from either end of the array followed by the player 2 and then play
# er 1 and so on. Each time a player picks a number, that number will not be avail
# able for the next player. This continues until all the scores have been chosen. 
# The player with the maximum score wins. 
# 
#  Given an array of scores, predict whether player 1 is the winner. You can ass
# ume each player plays to maximize his score. 
# 
#  Example 1: 
# 
#  
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2. 
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If playe
# r 2 chooses 5, then player 1 will be left with 1 (or 2). 
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
# Hence, player 1 will never be the winner and you need to return False.
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 
# and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to retu
# rn True representing player1 can win.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= length of the array <= 20. 
#  Any scores in the given array are non-negative integers and will not exceed 1
# 0,000,000. 
#  If the scores of both players are equal, then player 1 is still the winner. 
#  
#  Related Topics Dynamic Programming Minimax 
#  👍 1818 👎 103


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = self.dfs(nums, 0, len(nums) - 1, {})
        return ans >= 0

    def dfs(self, nums, i, j, memo):
        if i > j:
            return 0
        if i == j:
            return nums[i]
        if i + 1 == j:
            return abs(nums[i] - nums[j])
        if (i, j) in memo:
            return memo[(i, j)]

        lt = nums[i] - self.dfs(nums, i + 1, j, memo)
        rt = nums[j] - self.dfs(nums, i, j - 1, memo)
        memo[(i, j)] = max(lt, rt)
        return memo[(i, j)]
# leetcode submit region end(Prohibit modification and deletion)
