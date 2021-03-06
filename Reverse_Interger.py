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
        x = x * sign
        r = int(str(x)[::-1])
        return sign * r * (r < 0x7FFFFFFF)
        
        
class Solution3(object):       
    def reverse(self, x):
        if x>=0:
            res = int(str(x)[::-1])
        else:
            res = int('-' + str(x)[:0:-1])
        return res
        

class Solution4(object):       
    def reverse(self, x):
        result = 0
        pos_x = abs(x)
        while pos_x:
            result = result * 10 + pos_x % 10
            pos_x //= 10
        
        if result > 0x7FFFFFFF:
            return 0
            
        return result if x >= 0 else result * (-1)
        
if __name__ == '__main__':
    result = Solution4().reverse(12340)
    print(result)
        