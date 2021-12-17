class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # if start == end:
        #     return 0

        import collections
        bf = collections.deque([start])
        seen = set([start])
        step = 0

        while bf:
            nbf = collections.deque([])
            for node in bf:
                if node == end:
                    return step
                for possible in bank:
                    if self.onemute(node, possible):
                        if possible not in seen:
                            seen.add(possible)
                            nbf.append(possible)

            step += 1
            bf = nbf
        
        return -1 
    
    def onemute(self, node, possible):
        cnt = 0 
        for i in range(len(node)):
            if node[i] != possible[i]:
                cnt += 1 
                if cnt >= 2:
                    return False
        return True