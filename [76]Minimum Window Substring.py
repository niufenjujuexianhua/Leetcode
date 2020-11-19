# Given two strings s and t, return the minimum window in s which will contain a
# ll the characters in t. If there is no such window in s that covers all characte
# rs in t, return the empty string "". 
# 
#  Note that If there is such a window, it is guaranteed that there will always 
# be only one unique minimum window in s. 
# 
#  
#  Example 1: 
#  Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
#  Example 2: 
#  Input: s = "a", t = "a"
# Output: "a"
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 105 
#  s and t consist of English letters. 
#  
# 
#  
# Follow up: Could you find an algorithm that runs in O(n) time? Related Topics 
# Hash Table Two Pointers String Sliding Window 
#  👍 5462 👎 374


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m, n = len(s), len(t)
        if m < n:
            return ''

        dt = collections.Counter(t)
        need = len(dt)
        b = 0
        size, i, j = float('inf'), None, None

        for e, ch in enumerate(s):
            if ch in dt:
                dt[ch] -= 1
                if dt[ch] == 0:
                    need -= 1

            while need == 0:
                if e - b + 1 < size:
                    size = e - b + 1
                    i, j = b, e

                if s[b] in dt:
                    dt[s[b]] += 1
                    if dt[s[b]] > 0:
                        need += 1
                b += 1

        if size == float('inf'):
            return ''
        return s[i : j + 1]


        
# leetcode submit region end(Prohibit modification and deletion)
