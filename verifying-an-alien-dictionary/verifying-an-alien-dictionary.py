class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dt = {v : i for i, v in enumerate(order)}

        for word1, word2 in zip(words, words[1:]):
            m, n = len(word1), len(word2)
            for i in range(min(m, n)):
                if word1[i] != word2[i]:
                    if dt[word2[i]] < dt[word1[i]]:
                        return False
                    break
                    
                if i + 1 == min(m, n):
                    if m > n:
                        return False
        return True