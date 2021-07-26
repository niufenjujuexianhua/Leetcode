class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        used, seq = [0] * (n + 1), [0] * (2 * n - 1)
        self.dfs(used, seq, 0)
        return seq
        
        
    def dfs(self, used, seq, idx):
        if idx == len(seq):
            return True
        if seq[idx] != 0:
            return self.dfs(used, seq, idx + 1)
        
        for n in reversed(range(1, len(used))):
            if not used[n]:
                sec = idx + n 
                if n == 1:
                    sec = idx 
                
                if sec < len(seq) and seq[idx] == 0 and seq[sec] == 0:
                    used[n] = 1
                    seq[idx] = seq[sec] = n 
                    if self.dfs(used, seq, idx + 1):
                        return True
                    used[n] = 0
                    seq[idx] = seq[sec] = 0

        return False