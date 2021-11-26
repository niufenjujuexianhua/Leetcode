class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dt = {r: i for i, r in enumerate(list1)}
        
        res = [float('inf')]
        for i, r in enumerate(list2):
            if r in dt:
                if dt[r] + i == res[0]:
                    res.append(r)
                elif dt[r] + i < res[0]:
                    res = [dt[r] + i, r]
        return res[1:]
        