# Given a string s, a k duplicate removal consists of choosing k adjacent and eq
# ual letters from s and removing them causing the left and the right side of the 
# deleted substring to concatenate together. 
# 
#  We repeatedly make k duplicate removals on s until we no longer can. 
# 
#  Return the final string after all such duplicate removals have been made. 
# 
#  It is guaranteed that the answer is unique. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete. 
# 
#  Example 2: 
# 
#  
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa" 
# 
#  Example 3: 
# 
#  
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10^5 
#  2 <= k <= 10^4 
#  s only contains lower case English letters. 
#  
#  Related Topics Stack 
#  👍 864 👎 24


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        st = []
        for c in s:
            if st and c == st[-1][0]:
                st[-1][1] += 1
                if st[-1][1] == k:
                    st.pop()
            else:
                st.append([c, 1])

        return ''.join([c * cnt for c, cnt in st])




                # leetcode submit region end(Prohibit modification and deletion)
