class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        g = collections.defaultdict(list)
        self.build(root, g)
        # print(g)
        res, seen, q = [], {target.val}, collections.deque([(target.val, 0)])

        while q:
            node, dis = q.popleft()
            # print(node, dis)
            if dis == k:
                res.append(node)
            if dis + 1 <= k:
                for nei in g[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, dis + 1))
        return res

    def build(self, root, g):
        if not root:
            return

        if root.left:
            g[root.val].append(root.left.val)
            g[root.left.val].append(root.val)
        if root.right:
            g[root.val].append(root.right.val)
            g[root.right.val].append(root.val)
        self.build(root.left, g)
        self.build(root.right, g)