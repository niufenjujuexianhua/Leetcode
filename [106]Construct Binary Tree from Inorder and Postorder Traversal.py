# Given two integer arrays inorder and postorder where inorder is the inorder tr
# aversal of a binary tree and postorder is the postorder traversal of the same tr
# ee, construct and return the binary tree. 
# 
#  
#  Example 1: 
# 
#  
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  Example 2: 
# 
#  
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= inorder.length <= 3000 
#  postorder.length == inorder.length 
#  -3000 <= inorder[i], postorder[i] <= 3000 
#  inorder and postorder consist of unique values. 
#  Each value of postorder also appears in inorder. 
#  inorder is guaranteed to be the inorder traversal of the tree. 
#  postorder is guaranteed to be the postorder traversal of the tree. 
#  
#  Related Topics Array Tree Depth-first Search 
#  👍 2555 👎 48


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs(postorder, inorder, 0, len(postorder) - 1, 0, len(inorder) - 1)

    def dfs(self, postorder, inorder, sp, ep, si, ei):
        if sp > ep:
            return None
        if sp == ep:
            return TreeNode(postorder[sp])

        root = TreeNode(postorder[ep])
        idx = inorder.index(postorder[ep])
        lsize = idx - si
        root.left = self.dfs(postorder, inorder, sp, sp + lsize - 1, si, idx - 1)
        root.right = self.dfs(postorder, inorder, sp + lsize, ep - 1, idx + 1, ei)
        return root
        
# leetcode submit region end(Prohibit modification and deletion)
