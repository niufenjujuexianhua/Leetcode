class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        power = 0

        for i in range(len(digits)-1, -1, -1):
            sum += int(digits[i])*10**power
            power += 1
        return [int(i) for i in str(sum+1)]



class Solution2(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(str(x) for x in digits)) + 1
        return [int(x) for x in str(num)]



if __name__ == '__main__':
    result = Solution2().plusOne('7654')
    print(result)