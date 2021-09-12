class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        vcnt = sz = 1
        res = 0

        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                sz += 1
            elif word[i - 1] < word[i]:
                sz += 1
                vcnt += 1
            else:
                vcnt = sz = 1

            if vcnt == 5:
                res = max(res, sz)
        return res 