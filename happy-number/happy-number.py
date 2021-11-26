class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        
        while n != 1:
            if n in seen:
                return False 
            seen.add(n)
            
            nxt = 0 
            while n:
                nxt += (n % 10) ** 2 
                n //= 10
            n = nxt 
        return True 
                
        
        