class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0

        pre = self.kthGrammar(n - 1, (k + 1) // 2)
        if pre == 0:
            if k % 2 == 1:
                return 0 
            else:
                return 1 
        else:
            if k % 2 == 1:
                return 1
            else:
                return 0 
        
        