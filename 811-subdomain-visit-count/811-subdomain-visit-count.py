class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        import collections
        dt = collections.defaultdict(int)

        for cpdomain in cpdomains:
            n, domain = cpdomain.split(' ')
            dparts = domain.split('.')
            for i in reversed(range(len(dparts))):
                dt['.'.join(dparts[i:len(dparts)])] += int(n)

        res = []
        for d, n in dt.items():
            res.append(str(n) + ' ' + d)
        return res
        