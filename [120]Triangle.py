# Given a triangle, find the minimum path sum from top to bottom. Each step you 
# may move to adjacent numbers on the row below. 
# 
#  For example, given the following triangle 
# 
#  
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#  
# 
#  The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11). 
# 
#  Note: 
# 
#  Bonus point if you are able to do this using only O(n) extra space, where n i
# s the total number of rows in the triangle. 
#  Related Topics Array Dynamic Programming 
#  👍 2458 👎 273


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) <= 1: return 0 if not triangle else triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][0]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][-1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[-1])
# leetcode submit region end(Prohibit modification and deletion)
