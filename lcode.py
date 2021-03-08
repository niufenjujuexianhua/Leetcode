class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        order = sorted([(interval.start, 1) for interval in intervals] + [(interval.end, 0) for interval in intervals])

        res = cnt = 0
        for time, type in order:
            cnt += [-1, 1][type == 1]
            res = max(res, cnt)
        return res 