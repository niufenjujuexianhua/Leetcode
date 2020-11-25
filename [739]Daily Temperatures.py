# 
# Given a list of daily temperatures T, return a list such that, for each day in
#  the input, tells you how many days you would have to wait until a warmer temper
# ature. If there is no future day for which this is possible, put 0 instead.
#  
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 7
# 3], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#  
# 
#  Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
#  Related Topics Hash Table Stack 
#  👍 3468 👎 105


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(T)
        for i, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res
        
# leetcode submit region end(Prohibit modification and deletion)
