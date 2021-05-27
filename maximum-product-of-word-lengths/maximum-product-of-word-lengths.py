class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dt = {}
        for i, word in enumerate(words):
            s = 0
            for c in word:
                s |= 1 << (ord(c) - ord('a'))
            dt[i] = s

        res = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if dt[i] & dt[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res