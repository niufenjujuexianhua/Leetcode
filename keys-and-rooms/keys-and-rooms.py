class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = set([0])
        bf = set([0])
        
        while bf:
            nxt = set()
            for room in bf:
                for key in rooms[room]:
                    if key not in seen:
                        seen.add(key)
                        nxt.add(key)
                        
                        if len(seen) == len(rooms):
                            return True
            
            bf = nxt 
        return False