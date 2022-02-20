class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        neis = collections.defaultdict(list)
        for f, t, p in flights:
            neis[f].append((t, p))
            
        heap = [(0, -1, src)]
        seen_stops = collections.defaultdict(int)

        while heap:
            totalP, stops, city = heapq.heappop(heap)
            if city == dst:
                return totalP
            if stops == k:
                continue
            if city in seen_stops and seen_stops[city] <= stops:
                continue
            seen_stops[city] = stops
            
            for nei, neiP in neis[city]:
                heapq.heappush(heap, (totalP + neiP, stops + 1, nei))
        
        return -1