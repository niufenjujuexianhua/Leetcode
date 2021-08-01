class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = list(map(str, range(1, n + 1)))
        i = 2
        while i < n:
            res[i] = 'Fizz'
            i += 3

        j = 4
        while j < n:
            if res[j] != 'Fizz':
                res[j] = 'Buzz'
            else:
                res[j] += 'Buzz'
            j += 5
        return res