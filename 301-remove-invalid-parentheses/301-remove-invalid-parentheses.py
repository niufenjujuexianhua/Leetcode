class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        import  collections
        lt, rt, _ = self.valid(s)
        if lt == rt == 0:
            return [s]
        bf = collections.deque([s])
        seen = set([s])
        res = []
        while bf:
            sz = len(bf)
            found = False
            for _ in range(sz):
                ss = bf.popleft()

                if self.valid(ss)[2]:
                    res.append(ss)
                    found = True

                if not found:
                    for i, c in enumerate(ss):
                        if c in '()':
                            sss = ss[:i] + ss[i + 1:]
                            if sss not in seen:
                                seen.add(sss)
                                bf.append(sss)
            if found:
                break
        return res




    def valid(self, s):
        lt = rt = 0
        for c in s:
            if c == '(':
                lt += 1
            elif c == ')':
                if lt > 0:
                    lt -= 1
                else:
                    rt += 1
        return lt, rt, lt == rt == 0