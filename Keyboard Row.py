class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        res = []

        for i in words:
            for k in rows:
                a = set(i.lower())
                b = set(k.lower())
                if a.issubset(b):
                    res.append(i)
        return res


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [word for word in words if any(set(word.upper()) <= set(row) for row in ('QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM'))]

if __name__ == '__main__':
    result = Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(result)