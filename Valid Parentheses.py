# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:09:42 2017

@author: twu
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]','').replace('{}','')
            if len(s) == 0:
                return True
        return len(s) == 0


class Solution2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {')':'(', '}':'{', ']':'['}

        
        if len(s) == 0:
            return False
        
        stack = []
        for i in s:
            if stack and (i in dict and stack[-1] == dict[i]):
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0


        
        
if __name__ == '__main__':
    result = Solution2().isValid('()({}')
    print(result)
    
    
    
    
    
    
    
    
    
    
    