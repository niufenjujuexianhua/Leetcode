# One way to serialize a binary tree is to use preorder traversal. When we encou
# nter a non-null node, we record the node's value. If it is a null node, we recor
# d using a sentinel value such as '#'. 
# 
#  For example, the above binary tree can be serialized to the string "9,3,4,#,#
# ,1,#,#,2,#,6,#,#", where '#' represents a null node. 
# 
#  Given a string of comma-separated values preorder, return true if it is a cor
# rect preorder traversal serialization of a binary tree. 
# 
#  It is guaranteed that each comma-separated value in the string must be either
#  an integer or a character '#' representing null pointer. 
# 
#  You may assume that the input format is always valid. 
# 
#  
#  For example, it could never contain two consecutive commas, such as "1,,3". 
#  
# 
#  
#  Example 1: 
#  Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
#  Example 2: 
#  Input: preorder = "1,#"
# Output: false
#  Example 3: 
#  Input: preorder = "9,#,#,1"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= preorder.length <= 104 
#  preoder consist of integers in the range [0, 100] and '#' separated by commas
#  ','. 
#  
# 
#  
#  Follow up: Find an algorithm without reconstructing the tree. 
#  Related Topics Stack 
#  👍 938 👎 57


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        # i, slot = 0, 1
        # while i < len(preorder):
        #     if slot == 0:
        #         return False
        #
        #     if preorder[i] == '#':
        #         slot -= 1
        #     else:
        #         slot += 1
        #     i += 1
        # return slot == 0

        st = []
        for n in preorder:
            while n == '#' and st and st[-1] == '#':
                st.pop()
                if not st:
                    return False
                st.pop()
            st.append(n)
        return len(st) == 1 and st[-1] == '#'


# leetcode submit region end(Prohibit modification and deletion)
