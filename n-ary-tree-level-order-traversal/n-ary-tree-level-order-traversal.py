class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return
        res = []
        dq = collections.deque([root])
        while dq:
            sz = len(dq)
            res.append([])
            for _ in range(sz):
                node = dq.popleft()
                res[-1].append(node.val)
                for ch in node.children:
                    dq.append(ch)
        return res