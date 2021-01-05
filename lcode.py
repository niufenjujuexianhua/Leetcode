class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # write your code here
        # if not org: return not seqs or not seqs[0]
        import collections, functools
        if functools.reduce(set.union, seqs, set()) != set(org): return False
        n = len(org)
        indegree = [0] * (n + 1)
        graph = collections.defaultdict(list)

        for seq in seqs:
            for a, b in zip(seq, seq[1:]):
                indegree[b] += 1
                graph[a].append(b)

        dq = collections.deque([i for i in range(1, n + 1) if indegree[i] == 0])
        ls = []
        while dq:
            if len(dq) > 1:
                return False
            v = dq.popleft()
            ls.append(v)
            for nxt in graph[v]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    dq.append(nxt)
        return ls == org

    #     return True if self.dfs(graph, head[0], set([]), n) == 1 else False
    #
    # def dfs(self, graph, i, seen, n):
    #     if i in seen:
    #         return 0
    #
    #
    #     if len(seen) == n:
    #         return 1
    #
    #     seen.add(i)
    #     cnt = 0
    #     for nxt in graph[i]:
    #         cnt += self.dfs(graph, nxt, seen, n)
    #     return cnt + (len(seen) == n - 1 and i not in seen)
print(Solution().sequenceReconstruction([4,1,5,2,6,3],
[[5,2,6,3],[4,1,5,2]]))