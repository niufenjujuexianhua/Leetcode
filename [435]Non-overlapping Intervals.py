# Given a collection of intervals, find the minimum number of intervals you need
#  to remove to make the rest of the intervals non-overlapping. 
# 
#  
#  
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlappin
# g.
#  
# 
#  Example 2: 
# 
#  
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals non-ov
# erlapping.
#  
# 
#  Example 3: 
# 
#  
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're alrea
# dy non-overlapping.
#  
# 
#  
# 
#  Note: 
# 
#  
#  You may assume the interval's end point is always bigger than its start point
# . 
#  Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap
#  each other. 
#  
#  Related Topics Greedy 
#  👍 1917 👎 52


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        end, cnt = float('-inf'), 0
        for s, e in sorted(intervals, key = lambda x : x[1]):
            if s >= end:
                end = e
            else:
                cnt += 1
        return cnt
# leetcode submit region end(Prohibit modification and deletion)
