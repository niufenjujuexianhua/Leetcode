class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        import collections
        g = collections.defaultdict(dict)

        for a, b in redEdges:
            if 0 not in g[a]:
                g[a][0] = set()
            g[a][0].add(b)
        for a, b in blueEdges:
            if 1 not in g[a]:
                g[a][1] = set()
            g[a][1].add(b)


        bf = collections.deque([])
        seen = set()
        for color, nxts in g[0].items():
            for nxt in nxts:
                bf.append((color, nxt, 1))
                seen.add((color, nxt))
        
        res = [-1] * n 
        res[0] = 0 
        while bf:
            color, node, step = bf.popleft()
            if res[node] == -1:
                res[node] = step
            
            if node in g and 1 - color in g[node]:
            # for nxt in g[node][1 - color].values():
                nxts = g[node][1 - color]
                for nxt in nxts:
                    if (1 - color, nxt) not in seen:

                        seen.add((1 - color, nxt))
                        bf.append((1 - color, nxt, step + 1))
        return res 