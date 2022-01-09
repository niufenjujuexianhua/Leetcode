class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        import collections
        seen = collections.defaultdict(int)
        res = 0
        ss = ''

        for w in words:
            rev = w[::-1]
            if rev in seen and seen[rev] > 0:
                res += 4
                seen[rev] -= 1
            else:
                seen[w] = seen.get(w, 0) + 1

        for w in seen:
            if seen[w] > 0:
                if w[0] == w[1]:
                    res += 2
                    break
        return res