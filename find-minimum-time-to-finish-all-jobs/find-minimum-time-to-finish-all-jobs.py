class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        workers = [0] * k
        res = [float('inf')]
        self.dfs(jobs, 0, workers, res)
        return res[0]

    def dfs(self, jobs, i, workers, res):
        if i == len(jobs):
            res[0] = min(res[0], max(workers))
            return

        seen = set()
        for j in range(len(workers)):
            if workers[j] in seen: continue
            if workers[j] + jobs[i] >= res[0]: continue

            seen.add(workers[j])
            workers[j] += jobs[i]
            self.dfs(jobs, i + 1, workers, res)
            workers[j] -= jobs[i]
        