class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i = j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])

            if lo <= hi:
                res.append([lo, hi])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res