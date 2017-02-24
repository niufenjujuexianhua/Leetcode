class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        array = [None] * n
        array[0] = 1
        array[1] = 2

        for i in range(2, n):
            array[i] = array[i - 2] + array[i - 1]

        return array[n - 1]

class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-1)+self.climbStairs(n-2)

class Solution3(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a



if __name__ == '__main__':
    result = Solution3().climbStairs(7)
    print(result)