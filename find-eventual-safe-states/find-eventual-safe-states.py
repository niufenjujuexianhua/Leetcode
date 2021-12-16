class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # import collections
        # g = collections.defaultdict(set)
        # outdegree = [0] * len(graph)
        #
        # for i in range(len(graph)):
        #     for j in graph[i]:
        #         # g[j].add(i)
        #         outdegree[i] += 1

        seen = [0] * len(graph)
        # term = [0] * len(graph)
        # for i in outdegree:
        #     if outdegree[i] == 0:
        #         term[i] = 1

        order = []
        for i in range(len(graph)):
            # if seen[i] == 0:
            # seen = [0] * len(graph)
            if self.nocycle(graph, i, seen):
                order.append(i)

        return order

    def nocycle(self, g, cour, seen):
        if seen[cour] == 1:
            return True
        if seen[cour] == -1:
            return False

        seen[cour] = -1
        for nxt in g[cour]:
            if not self.nocycle(g, nxt, seen):
                return False

        seen[cour] = 1
        return True