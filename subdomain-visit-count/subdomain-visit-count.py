class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dt = collections.defaultdict(int)
        
        for entry in cpdomains:
            cnt, domain = entry.split(' ')
            domainparts = domain.split('.')

            for i in range(len(domainparts)):
                dt['.'.join(domainparts[i : ])] += int(cnt)

        res = []
        for key, val in dt.items():
            res.append(str(val) + ' ' + key)
        return res