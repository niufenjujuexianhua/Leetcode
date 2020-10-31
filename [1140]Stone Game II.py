# Alex and Lee continue their games with piles of stones. There are a number of 
# piles arranged in a row, and each pile has a positive integer number of stones p
# iles[i]. The objective of the game is to end with the most stones. 
# 
#  Alex and Lee take turns, with Alex starting first. Initially, M = 1. 
# 
#  On each player's turn, that player can take all the stones in the first X rem
# aining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). 
# 
#  The game continues until all the stones have been taken. 
# 
#  Assuming Alex and Lee play optimally, return the maximum number of stones Ale
# x can get. 
# 
#  
#  Example 1: 
# 
#  
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, th
# en Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex
#  takes two piles at the beginning, then Lee can take all three piles left. In th
# is case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= piles.length <= 100 
#  1 <= piles[i] <= 10 ^ 4 
#  
#  Related Topics Dynamic Programming 
#  👍 600 👎 146


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def stoneGameII(self, a):
        return self.dp(a, len(a), 0, 1, {})

    def dp(self, piles, n, s, m, memo):
        if s >= n:
            return 0

        if s + 2 * m >= n:
            return sum(piles[s:])

        if (s, m) in memo:
            return memo[(s, m)]

        total = sum(piles[s:])
        score = 0
        for x in range(1, 2 * m + 1):
            opponent = self.dp(piles, n, s + x, max(x, m), memo)
            score = max(score, total - opponent)

        memo[(s, m)] = score
        return score



    # leetcode submit region end(Prohibit modification and deletion)
