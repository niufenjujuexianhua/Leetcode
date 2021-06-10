class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        smallest = sum(mat[i][0] for i in range(m))
        hq = [[smallest] + [0] * m ]
        seen = set(tuple([0] * m))
        
        while k - 1:
            k -= 1
            prev = heapq.heappop(hq)
            
            for i in range(m):
                if prev[i + 1] == n - 1: continue
                total, idx = prev[0], prev[1:]
                
                total -= mat[i][idx[i]]
                idx[i] += 1 
                total += mat[i][idx[i]]
                
                if tuple(idx) not in seen:
                    seen.add(tuple(idx))
                    heapq.heappush(hq, [total] + idx)
        
        return heapq.heappop(hq)[0]