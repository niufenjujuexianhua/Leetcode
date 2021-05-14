class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        lt = self.flatten(root.left)
        rt = self.flatten(root.right)

        tmplt, tmprt = root.left, root.right
        root.left = root.right = None
        root.right = tmplt
        while root.right:
            root = root.right
        root.right = tmprt 