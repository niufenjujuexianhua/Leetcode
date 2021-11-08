# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        
        res = []
        self.dfs(root, res)
        return res 
        
    def dfs(self, root, res):
        if not root:
            return 
        
        
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)
        