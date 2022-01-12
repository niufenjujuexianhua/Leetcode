class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
             s1    e2
        s2     e2
        """
        if not firstList or not secondList:
            return []
        i = j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]

            if s1 <= s2 <= e1 or s2 <= s1 <= e2:
                res.append([max(s1, s2), min(e1, e2)])

            if e1 < e2:
                i += 1
            else:
                j += 1
        return res
