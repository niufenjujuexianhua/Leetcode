class Solution(object):
    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        aabbcc
        ab
        ij
        """
        import collections
        startWords = set([''.join(sorted(w)) for w in startWords])
        res = 0

        for w in targetWords:
            w = ''.join(sorted(w))
            i = j = 0
            while j < len(w):
                while j < len(w) and w[i] == w[j]:
                    j += 1
                if j - i == 1:
                    if w[:i] + w[i + 1:] in startWords:
                        res += 1
                        break
                i = j

        return res