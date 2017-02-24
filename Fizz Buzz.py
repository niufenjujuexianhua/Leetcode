class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [str(i) for i in range(1, n+1)]

        if n < 3:
            return res

        for i in range(2, len(res), 3):
            res[i] = 'Fizz'
        for k in range(4, len(res), 5):
            if res[k] == 'Fizz':
                res[k] = 'FizzBuzz'
            else: res[k] = 'Buzz'

        return res


class Solution2(object):
    def fizzBuzz(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

if __name__ == '__main__':
    result = Solution2().fizzBuzz(15)
    print(result)