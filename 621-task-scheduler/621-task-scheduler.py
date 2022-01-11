class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import collections
        import heapq
        n += 1
        dt = collections.Counter(tasks)
        res = 0
        hq = list(-cnt for cnt in dt.values())
        heapq.heapify(hq)
        while hq:
            k = min(len(hq), n)
            tmp = []
            for _ in range(k):
                cnt = heapq.heappop(hq)
                cnt += 1
                if cnt < 0:
                    tmp.append(cnt)

            if tmp:
                res += n
            else:
                res += k

            for cnt in tmp:
                heapq.heappush(hq, cnt)

        return res