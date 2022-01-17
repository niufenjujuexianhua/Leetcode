class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        import collections
        bank = set(bank)
        bank.discard(start)
        dt = collections.defaultdict(set)

        for w in bank:
            for i in range(len(w)):
                dt[w[:i] + '_' + w[i + 1:]].add(w)

        dq = collections.deque([(start, 0)])
        # seen = set([start])
        while dq:
            sz = len(dq)
            tmp = set()
            for _ in range(sz):
                w, step = dq.popleft()
                if w == end:
                    return step

                for i in range(len(w)):
                    for nxt in dt[w[:i] + '_' + w[i + 1:]]:
                        if nxt in bank:
                            tmp.add(nxt)
                            dq.append((nxt, step + 1))
            bank -= tmp
        return -1