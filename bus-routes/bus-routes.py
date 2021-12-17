class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        import collections
        if source == target:
            return 0

        g = collections.defaultdict(set)
        routes = list(map(set, routes))

        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if routes[i] & routes[j]:
                    g[i].add(j)
                    g[j].add(i)


        bf = collections.deque()
        targets = set()
        seen = set()
        for i in range(len(routes)):
            if source in routes[i]:
                bf.append(i)
                seen.add(i)
            if target in routes[i]:
                targets |= set([i])

        step = 1
        while bf:
            sz = len(bf)
            for _ in range(sz):
                i = bf.popleft()

                if i in targets:
                    return step


                for j in g[i]:
                    # for stop in routes[i]:
                    if j not in seen:
                        seen.add(j)
                        bf.append(j)

            step += 1

        return -1