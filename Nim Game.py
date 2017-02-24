class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        else:
            return True

class Solution2(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n % 4 == 0 else True

class Solution2(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n % 4)

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n & 3)


if __name__ == '__main__':
    result = Solution().canWinNim(33)
    print(result)