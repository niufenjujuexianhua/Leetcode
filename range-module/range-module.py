class Tree(object):
    def __init__(self, s, e, val):
        self.s = s
        self.e = e
        self.val = val
        self.left = None
        self.right = None


class RangeModule(object):

    def __init__(self):
        self.root = Tree(0, 10 ** 9, 0)

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        self.setStatus(self.root, left, right, 1)

    def setStatus(self, root, s, e, val):
        if s >= root.e or e <= root.s:
            return
        if s <= root.s and e >= root.e:
            root.left = None
            root.right = None
            root.val = val
            return

        m = root.s + (root.e - root.s) // 2
        if not root.left:
            root.left = Tree(root.s, m, root.val)
            root.right = Tree(m, root.e, root.val)


        self.setStatus(root.left, s, e, val)
        self.setStatus(root.right, s, e, val)
        root.val = root.left.val and root.right.val

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        return self.getStatus(self.root, left, right)

    def getStatus(self, root, s, e):
        if s >= root.e or e <= root.s:
            return 1
        if s <= root.s and e >= root.e:
            return root.val
        if not root.left:
            return root.val
        lt = self.getStatus(root.left, s, e)
        rt = self.getStatus(root.right, s, e)
        return lt and rt

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        self.setStatus(self.root, left, right, 0)