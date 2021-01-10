# A certain bug's home is on the x-axis at position x. Help them get there from 
# position 0. 
# 
#  The bug jumps according to the following rules: 
# 
#  
#  It can jump exactly a positions forward (to the right). 
#  It can jump exactly b positions backward (to the left). 
#  It cannot jump backward twice in a row. 
#  It cannot jump to any forbidden positions. 
#  
# 
#  The bug may jump forward beyond its home, but it cannot jump to positions num
# bered with negative integers. 
# 
#  Given an array of integers forbidden, where forbidden[i] means that the bug c
# annot jump to the position forbidden[i], and integers a, b, and x, return the mi
# nimum number of jumps needed for the bug to reach its home. If there is no possi
# ble sequence of jumps that lands the bug on position x, return -1. 
# 
#  
#  Example 1: 
# 
#  
# Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
# Output: 3
# Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
#  
# 
#  Example 2: 
# 
#  
# Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
# Output: -1
#  
# 
#  Example 3: 
# 
#  
# Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
# Output: 2
# Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will 
# get the bug home.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= forbidden.length <= 1000 
#  1 <= a, b, forbidden[i] <= 2000 
#  0 <= x <= 2000 
#  All the elements in forbidden are distinct. 
#  Position x is not forbidden. 
#  
#  Related Topics Dynamic Programming Breadth-first Search 
#  👍 168 👎 44


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        import collections
        bound = max(x, max(forbidden)) + a + b
        dq = collections.deque([[True, 0]])

        seen = set()
        seen.add((True, 0))
        seen.add((False, 0))
        for pos in forbidden:
            seen.add((True, pos))
            seen.add((False, pos))

        step = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                frd, node = dq.popleft()
                if node == x:
                    return step

                if (True, node + a) not in seen and node + a <= bound:
                    seen.add((True, node + a))
                    dq.append([True, node + a])

                if frd:
                    if node - b > 0 and (False, node - b) not in seen:
                        seen.add((False, node - b))
                        dq.append([False, node - b])

            step += 1
        return -1

print(Solution().minimumJumps([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
,29,
98,
80))
        
# leetcode submit region end(Prohibit modification and deletion)
