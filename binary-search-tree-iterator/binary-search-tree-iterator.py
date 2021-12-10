class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.st = []
        self.add(root)

    def next(self):
        """
        :rtype: int
        """
        node = self.st.pop()
        self.add(node.right)
        return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.st) != 0


    def add(self, node):
        while node:
            self.st.append(node)
            node = node.left