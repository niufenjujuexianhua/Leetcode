# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:18:59 2017

@author: twu

issue log:
    math.floor(math.log10(x)+1) is better than math.ceil(math.log10(x)) consider 10
    it should be n -= 2  not n -= 1
    
"""
import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
            
        y = 0
        temp = x
        
        while temp:
            y = y * 10 + temp % 10
            temp = temp // 10
      
#            remainder = temp % 10
#            temp = temp // 10
#            y = y * 10 + remainder

        return x == y
        
class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
            
        digit = math.floor(math.log10(x)+1)
        n = digit
        
        for i in range(digit//2):
            first_digit= x // math.pow(10, n-1) % 10
            last_digit = x % 10
            x = x // 10
            n -= 2
            if first_digit != last_digit:
                return False
        return True
        

        
if __name__ == '__main__':
    result = Solution2().isPalindrome(10)
    print(result)



