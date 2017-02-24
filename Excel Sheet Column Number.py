class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        sum = 0

        for i, v in enumerate(s):
            sum += (ord(v) - 64) * 26 ** (length-i-1)
        return sum
        # return sum((ord(v) - 64) * 26 ** (length-i-1) for i, v in enumerate(s))



if __name__ == '__main__':
    result = Solution().titleToNumber('AB')
    print(result)