class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]

        return (max([b - a for a, b in zip(horizontalCuts, horizontalCuts[1:])]) * \
               max([b - a for a, b in zip(verticalCuts, verticalCuts[1:])])) % (10 ** 9 + 7)