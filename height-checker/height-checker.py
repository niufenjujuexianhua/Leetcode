class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum([int(a != b) for a, b in zip(sorted(heights), heights)])