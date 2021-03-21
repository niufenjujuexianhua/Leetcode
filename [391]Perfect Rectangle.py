# Given N axis-aligned rectangles where N > 0, determine if they all together fo
# rm an exact cover of a rectangular region. 
# 
#  Each rectangle is represented as a bottom-left point and a top-right point. F
# or example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-lef
# t point is (1, 1) and top-right point is (2, 2)). 
# 
#  
# 
#  Example 1: 
# 
#  
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [3,2,4,4],
#   [1,3,2,4],
#   [2,3,3,4]
# ]
# 
# Return true. All 5 rectangles together form an exact cover of a rectangular re
# gion.
#  
# 
#  
# 
#  
# 
#  
# 
#  Example 2: 
# 
#  
# rectangles = [
#   [1,1,2,3],
#   [1,3,2,4],
#   [3,1,4,2],
#   [3,2,4,4]
# ]
# 
# Return false. Because there is a gap between the two rectangular regions.
#  
# 
#  
# 
#  
# 
#  
# 
#  Example 3: 
# 
#  
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [3,2,4,4]
# ]
# 
# Return false. Because there is a gap in the top center.
#  
# 
#  
# 
#  
# 
#  
# 
#  Example 4: 
# 
#  
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [2,2,4,4]
# ]
# 
# Return false. Because two of the rectangles overlap with each other.
#  
# 
#  Related Topics Line Sweep 
#  👍 452 👎 86


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        corners = set()
        area = 0
        for x1, y1, x2, y2 in rectangles:
            for x, y in [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]:
                if (x, y) in corners:
                    corners.remove((x, y))
                else:
                    corners.add((x, y))

            area += (x2 - x1) * (y2 - y1)
        if len(corners) != 4:
            return False

        corners = sorted(corners)
        return (corners[-1][0] - corners[0][0]) * (corners[-1][1] - corners[0][1]) == area
# print(Solution().isRectangleCover([
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [2,2,4,4]
# ]
# ))
# leetcode submit region end(Prohibit modification and deletion)
