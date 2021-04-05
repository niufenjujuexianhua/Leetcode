# Given two integer arrays preorder and inorder where preorder is the preorder t
# raversal of a binary tree and inorder is the inorder traversal of the same tree,
#  construct and return the binary tree. 
# 
#  
#  Example 1: 
# 
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  Example 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= preorder.length <= 3000 
#  inorder.length == preorder.length 
#  -3000 <= preorder[i], inorder[i] <= 3000 
#  preorder and inorder consist of unique values. 
#  Each value of inorder also appears in preorder. 
#  preorder is guaranteed to be the preorder traversal of the tree. 
#  inorder is guaranteed to be the inorder traversal of the tree. 
#  
#  Related Topics Array Tree Depth-first Search 
#  👍 4971 👎 128


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def dfs(self, preorder, inorder, sp, ep, si, ei):
        if sp > ep:
            return None
        if sp == ep:
            return TreeNode(preorder[sp])

        root = TreeNode(preorder[sp])
        idx = inorder.index(preorder[sp])
        lsize, rsize = idx - si, ei - idx
        root.left = self.dfs(preorder, inorder, sp + 1, sp + lsize, si, idx - 1)
        root.right = self.dfs(preorder, inorder, sp + lsize + 1, ep, idx + 1, ei)
        return root
# leetcode submit region end(Prohibit modification and deletion)
