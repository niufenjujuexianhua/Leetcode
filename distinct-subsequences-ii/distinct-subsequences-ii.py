class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10 ** 9 + 7
        ends = [0] * 26
        for ss in s:
            ends[ord(ss) - ord('a')] = sum(ends) + 1
        return sum(ends) % mod