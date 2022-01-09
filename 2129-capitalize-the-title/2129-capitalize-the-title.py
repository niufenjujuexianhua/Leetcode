class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split(' ')
        ls = [] 
        for w in words:
            if len(w) <= 2:
                ls.append(w.lower())
            else:
                ls.append(w.title())
        return ' '.join(ls)
