# Given preorder and inorder traversal of a tree, construct the binary tree. 
# 
#  Note: 
# You may assume that duplicates do not exist in the tree. 
# 
#  For example, given 
# 
#  
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7] 
# 
#  Return the following binary tree: 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7 
#  Related Topics Array Tree Depth-first Search 
#  👍 4085 👎 109


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return
        indices = {k: v for v, k in enumerate(inorder)}

        return self.helper(preorder, 0, len(preorder) - 1,
                            inorder, 0, len(inorder) - 1, indices)

    def helper(self, preorder, plt, prt,
                     inorder, ilt, irt, indices):
        if plt > prt:
            return None
        if plt == prt:
            return TreeNode(preorder[plt])

        root = TreeNode(preorder[plt])
        idx = indices[preorder[plt]]
        ltsize = idx - ilt

        root.left = self.helper(preorder, plt + 1, plt + ltsize,
                                inorder, ilt, idx - 1, indices)
        root.right = self.helper(preorder, plt + ltsize + 1, prt,
                                inorder, idx + 1, irt, indices)
        return root



        # leetcode submit region end(Prohibit modification and deletion)
