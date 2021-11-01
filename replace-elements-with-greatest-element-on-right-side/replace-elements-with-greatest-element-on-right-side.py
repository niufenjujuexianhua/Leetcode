class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        import heapq
        hq = []
        for i, a in enumerate(arr):
            heapq.heappush(hq, (-a, i))

        for i, a in enumerate(arr):
            if i == len(arr) - 1:
                arr[i] = -1
                break

            while hq and hq[0][1] <= i:
                heapq.heappop(hq)
            arr[i] = -hq[0][0]
        return arr