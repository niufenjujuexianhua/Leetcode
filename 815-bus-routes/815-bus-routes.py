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

        dt = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                dt[stop].add(i)


        seenstop = set([source])
        seenroute = set()
        bf = collections.deque([(source, 0)])

        while bf:
            sz = len(bf)
            for _ in range(sz):
                stop, step = bf.popleft()
                if stop == target:
                    return step
                
                for rid in dt[stop]:
                    if rid not in seenroute:
                        seenroute.add(rid)
                        for nxtstop in routes[rid]:
                            if nxtstop not in seenstop:
                                seenstop.add(nxtstop)
                                bf.append((nxtstop, step + 1))
                                # step += 1
        return -1