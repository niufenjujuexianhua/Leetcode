class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        node = root 
        while True:
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    break 
                else:
                    node = node.left
    
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right


        return root