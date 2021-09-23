class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        1 2
        0 1
        i j
        0 1 2
        i  i + 1  j+1
        """
        n = len(stones)
        
        prefix = [0]
        for i in stones:
            prefix.append(prefix[-1]+i)
        
        dp = [[-1]*n for _ in range(n)]
        
        def solve(left, right):
            if left == right:
                return 0
            
            if dp[left][right]!=-1:
                return dp[left][right]
            
            leftScore = prefix[right+1] - prefix[left+1] - solve(left+1,right)
            rightScore = prefix[right] - prefix[left] - solve(left,right-1)
            
            dp[left][right] = max(leftScore,rightScore)
            return dp[left][right]
        
        return solve(0,n-1)