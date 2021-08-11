class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dt = collections.defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            dt[key].append(word)
        return dt.values()