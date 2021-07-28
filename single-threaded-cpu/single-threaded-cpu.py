class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        import heapq
        tasks = sorted([(s, t, i) for i, (s, t) in enumerate(tasks)])
        idx = 0
        time = 0
        res = []
        hq = []
        while hq or idx < len(tasks):
            while idx < len(tasks) and tasks[idx][0] <= time:
                heapq.heappush(hq, (tasks[idx][1], tasks[idx][2]))
                idx += 1

            if hq:
                t, i = heapq.heappop(hq)
                res.append(i)
                time += t
            elif idx < len(tasks):
                time = tasks[idx][0]


        return res