class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = []
        for i in bin(num)[2:]:
            if i == '1':
                res.append(0)
            else:
                res.append(1)

        return int(''.join(map(str,res)), 2)


class Solution2(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(str(1 - int(x)) for x in bin(num)[2:]), 2)

class Solution3(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = 1 << (len(bin(num)) - 2)
        return (mask - 1) ^ num

class Solution4(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        msb = num.bit_length()
        return (2**msb-1) ^ num

if __name__ == '__main__':
    result = Solution4().findComplement(5)
    print(result)