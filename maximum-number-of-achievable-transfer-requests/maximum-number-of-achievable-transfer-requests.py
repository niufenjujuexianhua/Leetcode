class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        nr = len(requests)
        res = 0 

        for mask in range((1 << nr) - 1, 0, -1):
            building = [0] * n
            cnt = 0
            for i in range(nr):
                if mask & (1 << i):
                    cnt += 1
                    building[requests[i][0]] -= 1
                    building[requests[i][1]] += 1
            if all(b == 0 for b in building):
                res = max(res, cnt)
        return res