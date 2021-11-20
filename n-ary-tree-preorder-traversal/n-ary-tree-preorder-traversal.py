class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = [root]
        res = [] 
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)

                stack.extend(node.children[::-1])
        return res 