class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key = lambda x : x[1])
        hq = [] 
        day = 0
        res = 0
        for dur, ddl in courses:
            heapq.heappush(hq, -dur)
            day += dur
            res += 1
            if day > ddl:
                day += heapq.heappop(hq)
                res -= 1
        return res