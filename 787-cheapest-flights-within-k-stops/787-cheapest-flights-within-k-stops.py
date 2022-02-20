class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        visited = {}
        graph = collections.defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))
        heap = [(0, 0, src)]
        while heap:
            dist, moves, node = heapq.heappop(heap)
            if node == dst and K >= moves - 1:
                return dist
            if node not in visited or visited[node] > moves:
                visited[node] = moves
                for nei, weight in graph[node]:
                    heapq.heappush(heap, (dist + weight, moves + 1, nei))
        return -1