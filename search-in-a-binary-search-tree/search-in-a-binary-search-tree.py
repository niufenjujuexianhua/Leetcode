class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return 
        while root:
            if root.val == val:
                return root 
            elif root.val < val:
                root = root.right 
            else:
                root = root.left 
        return 