class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        for i in range(len(num1)):
            res += (ord(num1[i]) - ord('0'))*10**(len(num1)-i-1)
        for k in range(len(num2)):
            res += (ord(num2[k]) - ord('0')) *10** (len(num2) - k - 1)
        return str(res)



if __name__ == '__main__':
    result = Solution().addStrings('9','99')
    print(result)