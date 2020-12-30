# Given an array points containing the coordinates of points on a 2D plane, sort
# ed by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i 
# < j <= points.length. You are also given an integer k. 
# 
#  Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <=
#  k and 1 <= i < j <= points.length. It is guaranteed that there exists at least 
# one pair of points that satisfy the constraint |xi - xj| <= k. 
# 
#  
#  Example 1: 
# 
#  
# Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# Output: 4
# Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if 
# we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points al
# so satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
# No other pairs satisfy the condition, so we return the max of 4 and 1. 
# 
#  Example 2: 
# 
#  
# Input: points = [[0,0],[3,0],[9,2]], k = 3
# Output: 3
# Explanation: Only the first two points have an absolute difference of 3 or les
# s in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= points.length <= 10^5 
#  points[i].length == 2 
#  -10^8 <= points[i][0], points[i][1] <= 10^8 
#  0 <= k <= 2 * 10^8 
#  points[i][0] < points[j][0] for all 1 <= i < j <= points.length 
#  xi form a strictly increasing sequence. 
#  
#  Related Topics Array Sliding Window 
#  👍 246 👎 8


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        st, res = collections.deque([]), float('-inf')
        for x, y in points:
            while st and x - st[0][1] > k:
                st.popleft()
            if st:
                res = max(res, st[0][0] + x + y)
            while st and y - x >= st[-1][0]:
                st.pop()
            st.append((y - x, x))
        return res

        
# leetcode submit region end(Prohibit modification and deletion)
