class Solution(object):
    def minInterval(self, A, queries):
        import heapq
        A.sort()
        queries = sorted([(q, i) for i, q in enumerate(queries)])
        res = [-1] * len(queries)

        idx = 0
        hq = []

        for q, i in queries:
            while idx < len(A) and A[idx][0] <= q:
                if A[idx][1] >= q:
                    heapq.heappush(hq, (A[idx][1] - A[idx][0] + 1, A[idx][1]))
                idx += 1

            while hq and hq[0][1] < q:
                heapq.heappop(hq)

            if hq:
                res[i] = hq[0][0]
        return res
        