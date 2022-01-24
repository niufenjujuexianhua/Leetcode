class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import collections
        bf = collections.deque([(root, 0, 0)])
        dt = collections.defaultdict(list)
        cmin, cmax = float('inf'), float('-inf')

        while bf:
            # sz = len(bf)
            # for _ in range(sz):
            node, r, c = bf.popleft()
            # if r not in dt[c]:
            #     dt[c][r] = []
            dt[c].append((r, node.val))
            # if len(dt[c][r]) >= 2:
            #     dt[c][r] = sorted(dt[c][r])
            cmin = min(cmin, c)
            cmax = max(cmax, c)
            if node.left:
                bf.append((node.left, r + 1, c - 1))
            if node.right:
                bf.append((node.right, r + 1, c + 1))

        res = []
        for c in range(cmin, cmax + 1):
            # tmp = [v for r, v in dt[c].items()]
            res.append(v for r, v in sorted(dt[c]))
        return res
