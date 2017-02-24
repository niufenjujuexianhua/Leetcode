class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        carry = 0

        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        else:
            b = '0' * (len(a) - len(b)) + b

        for i in range(len(a) - 1, -1, -1):
            temp = carry
            x = int(a[i])
            y = int(b[i])
            carry = (x + y + temp) // 2
            res.insert(0, str((x + y + temp) % 2))

        if carry:
            res.insert(0, '1')
        return ''.join(res)

if __name__ == '__main__':
    result = Solution().addBinary('1010', '111')
    print(result)