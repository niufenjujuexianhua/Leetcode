# There are n cities connected by m flights. Each flight starts from city u and 
# arrives at v with a price w. 
# 
#  Now given all the cities and flights, together with starting city src and the
#  destination dst, your task is to find the cheapest price from src to dst with u
# p to k stops. If there is no such route, output -1. 
# 
#  
# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as mar
# ked red in the picture. 
# 
#  
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as mar
# ked blue in the picture.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes n will be in range [1, 100], with nodes labeled from 0 to
#  n - 1. 
#  The size of flights will be in range [0, n * (n - 1) / 2]. 
#  The format of each flight will be (src, dst, price). 
#  The price of each flight will be in the range [1, 10000]. 
#  k is in the range of [0, n - 1]. 
#  There will not be any duplicated flights or self cycles. 
#  
#  Related Topics Dynamic Programming Heap Breadth-first Search 
#  👍 2656 👎 88


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        import heapq, collections
        graph = collections.defaultdict(dict)
        for s, d, c in flights:
            graph[s][d] = c

        bfs = [(0, src, 0)]
        heapq.heapify(bfs)
        while bfs:
            cost, src, stop = heapq.heappop(bfs)

            if src == dst: return cost

            for nxt in graph[src]:
                if stop < K + 1:
                    heapq.heappush(bfs, (cost + graph[src][nxt], nxt, stop + 1))
        return -1

print(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]],
src = 0, dst = 2, K = 1))
        
# leetcode submit region end(Prohibit modification and deletion)
