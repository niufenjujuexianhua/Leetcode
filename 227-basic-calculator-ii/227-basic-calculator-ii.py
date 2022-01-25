class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return
        n, prevSign, stack = 0, '+', []
        for i in range(len(s)):
            if s[i].isdigit():
                n = n * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if prevSign == '+':
                    stack.append(n)
                elif prevSign == '-':
                    stack.append(-n)
                elif prevSign == '*':
                    stack.append(stack.pop() * n)
                else:
                    last = stack.pop()
                    # if last < 0:
                    #     stack.append(-(-last // n))
                    # else:
                    #     stack.append(last // n)
                    stack.append(int(last / float(n)))
                n = 0
                prevSign = s[i]

        return sum(stack)
# print(Solution().calculate(" 3/2 "))


        
