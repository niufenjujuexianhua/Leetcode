# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 19:44:06 2017

@author: twu

if get time, rewrite the code. try to make it as concise as possible
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """               
        sign = -1 if x < 0 else 1
        x = x*sign
        
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x = x//10
        
        if y > 0x7FFFFFFF:
            return 0

        return y*sign

class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """ 
        sign = -1 if x < 0 else 1
        x = x*sign
        r = sign*int(str(x)[::-1])
        return r * (r < 2**31)

        
        
if __name__ == '__main__':
    result = Solution().reverse(12340)
    print(result)
        