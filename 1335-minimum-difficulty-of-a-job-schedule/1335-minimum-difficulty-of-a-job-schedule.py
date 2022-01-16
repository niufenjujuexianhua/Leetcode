class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        res = self.dfs(jobDifficulty, 0, d, {})
        return res if res != float('inf') else -1 


    def dfs(self, jobs, i, d, dp):
        if i == len(jobs) or d == 0:
            if  i == len(jobs) and d == 0:
                return 0
            return float('inf')
        
        if (i, d) in dp:
            return dp[(i, d)]
        
        if d == 1:
            return max(jobs[i:])
        

        # if d > len(jobs) - i:
        #     return float('inf')

        # xyzabc
        #d = 3
        maxn = jobs[i]
        res = float('inf')
        for j in range(i, len(jobs) - d + 1):
            maxn = max(maxn, jobs[j])
            res = min(res,
                      maxn + self.dfs(jobs, j + 1, d - 1, dp))
        dp[(i, d)] = res 
        return res