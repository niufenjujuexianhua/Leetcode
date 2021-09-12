class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # print(','.join(map(str, self.preorder(root))))
        if not root:
            return ''
        return ','.join(map(str, self.preorder(root)))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return [] 
        return self.deser(collections.deque(data.split(',')), float('-inf'), float('inf'))

    def deser(self, ls, lo, hi):
        if ls and lo < int(ls[0]) < hi:
            # root = int(ls.popleft())
            # if not lo < root < hi:
            #     return None

            root = TreeNode(int(ls.popleft()))
            root.left = self.deser(ls, lo, root.val)
            root.right = self.deser(ls, root.val, hi)
            return root

    def preorder(self, root):
        if not root:
            return []

        return [root.val] + self.preorder(root.left) + self.preorder(root.right)