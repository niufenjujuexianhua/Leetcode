# Given the integer n representing the number of courses at some university labe
# led from 1 to n, and the array dependencies where dependencies[i] = [xi, yi] rep
# resents a prerequisite relationship, that is, the course xi must be taken before
#  the course yi. Also, you are given the integer k. 
# 
#  In one semester you can take at most k courses as long as you have taken all 
# the prerequisites for the courses you are taking. 
# 
#  Return the minimum number of semesters to take all courses. It is guaranteed 
# that you can take all courses in some way. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
# Output: 3 
# Explanation: The figure above represents the given graph. In this case we can 
# take courses 2 and 3 in the first semester, then take course 1 in the second sem
# ester and finally take course 4 in the third semester.
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
# Output: 4 
# Explanation: The figure above represents the given graph. In this case one opt
# imal way to take all courses is: take courses 2 and 3 in the first semester and 
# take course 4 in the second semester, then take course 1 in the third semester a
# nd finally take course 5 in the fourth semester.
#  
# 
#  Example 3: 
# 
#  
# Input: n = 11, dependencies = [], k = 2
# Output: 6
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 15 
#  1 <= k <= n 
#  0 <= dependencies.length <= n * (n-1) / 2 
#  dependencies[i].length == 2 
#  1 <= xi, yi <= n 
#  xi != yi 
#  All prerequisite relationships are distinct, that is, dependencies[i] != depe
# ndencies[j]. 
#  The given graph is a directed acyclic graph. 
#  
#  Related Topics Graph 
#  👍 268 👎 27


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minNumberOfSemesters(self, n, dependencies, k):
        """
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
        """
        dp = [float('inf')] * (1 << n)
        prevState = [0] * (1 << n)
        prevCourse = [0] * n

        for a, b in dependencies:
            prevCourse[b - 1] |= 1 << (a - 1)

        for state in range(1 << n):
            prevState[state] = 0
            for i in range(n):
                if (state >> i) & 1:
                    prevState[state] |= prevCourse[i]

        dp[0] = 0
        for state in range(1, (1 << n)):
            subset = state
            while subset >= 0:
                subset = (subset - 1) & state
                if (self.cnt(state) - self.cnt(subset) <= k and
                    (prevState[state] & subset) == prevState[state]):
                    dp[state] = min(dp[state], dp[subset] + 1)
                if subset == 0:
                    break
        return dp[-1]

    def cnt(self, state):
        res = 0
        while state:
            res += state & 1
            state >>= 1
        return res

print(Solution().minNumberOfSemesters(15,
[[2,1]],
4))

        
# leetcode submit region end(Prohibit modification and deletion)
