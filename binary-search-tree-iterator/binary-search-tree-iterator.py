class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.st = []
        node = root 
        # self.node = root

        # while self.st or self.node:
        while node:
            self.st.append(node)
            node = node.left
            # else:
            #     cur = self.st.pop()
            #     print(cur.val)
            #     self.node = cur.right
        

    def next(self):
        """
        :rtype: int
        """
        if self.st:
            cur = self.st.pop()
            node = cur.right 
            while node:
                self.st.append(node)
                node = node.left 
            return cur.val 
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.st != [] 