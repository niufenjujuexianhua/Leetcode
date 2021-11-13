# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, float('-inf'), float('inf'))
    def dfs(self, node, mn, mx):
        if not node:
            return True
        if mn >= node.val or mx <= node.val:
            return False

        return self.dfs(node.left, mn, node.val) and self.dfs(node.right, node.val, mx)
        