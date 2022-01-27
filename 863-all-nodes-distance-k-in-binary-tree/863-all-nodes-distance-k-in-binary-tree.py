class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        import collections
        g = collections.defaultdict(set)
        self.build(root, g, None)
        # print(g)

        bf = collections.deque([target.val])
        seen = set([target.val])
        for i in range(k):
            sz = len(bf)
            for _ in range(sz):
                val = bf.popleft()

                for nxt in g[val]:
                    if nxt not in seen:
                        seen.add(nxt)
                        bf.append(nxt)
            # print(bf)
        return list(bf)


    def build(self, root, g, par):
        if not root:
            return
        if par is not None:
            g[par].add(root.val)
            g[root.val].add(par)

        self.build(root.left, g, root.val)
        self.build(root.right, g, root.val)