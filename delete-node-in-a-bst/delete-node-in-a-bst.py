class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        no lt, no rt:
            remove key
        no lt, rt:
            replace with rt tree root
        lt, no rt:
            replace with lt tree root
        lt, rt:
            replace key val with leftmost node of the right tree
        """
        if not root:
            return
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root 
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left 
            
            tmp = root.right 
            while tmp.left:
                tmp = tmp.left 
            root.val = tmp.val 
            root.right = self.deleteNode(root.right, tmp.val)
            return root 