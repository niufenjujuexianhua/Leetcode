# There are N network nodes, labelled 1 to N. 
# 
#  Given times, a list of travel times as directed edges times[i] = (u, v, w), w
# here u is the source node, v is the target node, and w is the time it takes for 
# a signal to travel from source to target. 
# 
#  Now, we send a signal from a certain node K. How long will it take for all no
# des to receive the signal? If it is impossible, return -1. 
# 
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2
#  
# 
#  
# 
#  Note: 
# 
#  
#  N will be in the range [1, 100]. 
#  K will be in the range [1, N]. 
#  The length of times will be in the range [1, 6000]. 
#  All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100. 
#  
#  Related Topics Heap Depth-first Search Breadth-first Search Graph 
#  👍 2249 👎 242


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        import heapq, collections
        graph = collections.defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w

        hq = [(0, K)]
        seen = {}
        while hq:
            d, u = heapq.heappop(hq)
            if u in seen: continue
            seen[u] = d
            for v in graph[u]:
                if v not in seen:
                    heapq.heappush(hq, (d + graph[u][v], v))
        return max(seen.values()) if len(seen) == N else -1


print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2))
# leetcode submit region end(Prohibit modification and deletion)
