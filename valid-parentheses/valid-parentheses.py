class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        map = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c not in map:
                stack.append(c)
            elif c in map and stack and stack[-1] == map[c]:
                stack.pop()
            else:
                return False
        return not stack
            