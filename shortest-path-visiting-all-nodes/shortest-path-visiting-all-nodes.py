class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        import collections
        n = len(graph)
        target = (1 << n) - 1

        q = collections.deque()
        seen = set()
        for i in range(n):
            q.append((1 << i, i, 0))
            seen.add((1 << i, i))

        while q:
            visited, node, cost = q.popleft()
            if visited == target:
                return cost

            for nxt in graph[node]:
                if (visited | (1 << nxt), nxt) not in seen:
                    seen.add((visited | (1 << nxt), nxt))
                    q.append((visited | (1 << nxt), nxt, cost + 1))
        return -1 