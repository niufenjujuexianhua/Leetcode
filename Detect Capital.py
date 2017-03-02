class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = 0
        n = sum(map(lambda x: x.isupper(), word))

        return n == 0 or n == len(word) or (n == 1 and word[0].isupper())

class Solution2(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()

if __name__ == '__main__':
    result = Solution().detectCapitalUse("USA")
    print(result)