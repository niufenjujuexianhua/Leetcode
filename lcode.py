class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        # write your code here
        if not root:
            return

        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        succ = None
        while root:
            if root.val > p.val:
                succ = root
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                break
        return succ