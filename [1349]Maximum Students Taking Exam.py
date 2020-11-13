# Given a m * n matrix seats that represent seats distributions in a classroom. 
# If a seat is broken, it is denoted by '#' character otherwise it is denoted by a
#  '.' character. 
# 
#  Students can see the answers of those sitting next to the left, right, upper 
# left and upper right, but he cannot see the answers of the student sitting direc
# tly in front or behind him. Return the maximum number of students that can take 
# the exam together without any cheating being possible.. 
# 
#  Students must be placed in seats in good condition. 
# 
#  
#  Example 1: 
# 
#  
# Input: seats = [["#",".","#","#",".","#"],
#                 [".","#","#","#","#","."],
#                 ["#",".","#","#",".","#"]]
# Output: 4
# Explanation: Teacher can place 4 students in available seats so they don't che
# at on the exam. 
#  
# 
#  Example 2: 
# 
#  
# Input: seats = [[".","#"],
#                 ["#","#"],
#                 ["#","."],
#                 ["#","#"],
#                 [".","#"]]
# Output: 3
# Explanation: Place all students in available seats. 
# 
#  
# 
#  Example 3: 
# 
#  
# Input: seats = [["#",".",".",".","#"],
#                 [".","#",".","#","."],
#                 [".",".","#",".","."],
#                 [".","#",".","#","."],
#                 ["#",".",".",".","#"]]
# Output: 10
# Explanation: Place students in available seats in column 1, 3 and 5.
#  
# 
#  
#  Constraints: 
# 
#  
#  seats contains only characters '.' and'#'. 
#  m == seats.length 
#  n == seats[i].length 
#  1 <= m <= 8 
#  1 <= n <= 8 
#  
#  Related Topics Dynamic Programming 
#  👍 343 👎 9


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        m, n = len(seats), len(seats[0])
        dp = [[0] * (1 << n) for _ in range(m + 1)]

        s = [0]
        for i in range(m):
            state = 0
            for j in range(n):
                state |= (seats[i][j] == '#') << j
            s.append(state)

        for i in range(1, m + 1):
            for cstate in range(1 << n):
                if cstate & s[i] or cstate & (cstate >> 1): continue
                for lstate in range(1 << n):
                    if not lstate & (cstate >> 1) and not (lstate >> 1) & cstate and not lstate & s[i - 1]:
                        dp[i][cstate] = max(dp[i][cstate], dp[i - 1][lstate] + self.cnt(cstate))

        return max(dp[-1])

    def cnt(self, state):
        res = 0
        while state:
            res += (state & 1)
            state >>= 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
