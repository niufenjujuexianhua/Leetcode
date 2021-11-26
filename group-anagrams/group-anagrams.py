class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dt = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            dt[key].append(s)
        return list(dt.values())