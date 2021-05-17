class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordsset = set(words)
        m = {}
        for word in wordsset:
            self.dfs(wordsset, word, m)
        res = max(m.values())
        return res 

    def dfs(self, wordsset, word, m):
        if word not in wordsset:
            return 0
        if word in m:
            return m[word]

        ans = 0
        for i in range(len(word)):
            nword = word[:i] + word[i + 1:]
            ans = max(ans, self.dfs(wordsset, nword, m))

        m[word] = ans + 1
        return m[word]