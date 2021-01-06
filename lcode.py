class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        # Write your code here
        import collections
        chars = set(''.join(words))
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)

        for prev, succ in zip(words, words[1:]):
            for i in range(len(prev)):
                if i >= len(succ):
                    return ''
                if prev[i] != succ[i]:
                    if prev[i] in graph[succ[i]]:
                        return ''
                    indegree[succ[i]] += 1
                    graph[prev[i]].append(succ[i])
                    break

        hq = collections.deque([ch for ch in chars if indegree[ch] == 0])
        res = ''
        while hq:
            node = hq.popleft()
            res += node
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    hq.append(nxt)
        return res * (len(res) == len(chars))

    # def dfs(self, graph, node, seen):
    #     if node in seen:
    #         return ''
    #
    #     seen.add(node)
    #     for nxt in sorted(graph[node]):
    #         node += self.dfs(graph, nxt, seen)
    #     return node

print(Solution().alienOrder(["zy","zx"]))