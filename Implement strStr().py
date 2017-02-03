# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 23:10:02 2017

@author: twu
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
        
        
if __name__ == '__main__':
    result = Solution().strStr("","")
    print(result)
