class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        s = sum(cardPoints[:k])
        res = s
        for i in range(1, k + 1):
            s += cardPoints[-i] - cardPoints[k - i]
            res = max(res, s)
        return res