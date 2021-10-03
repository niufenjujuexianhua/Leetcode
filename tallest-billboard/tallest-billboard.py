class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        dt = {0:0}
        for r in rods:
            ndt = {}
            for ss, mx in dt.items():
                ndt[ss + r] = max(ndt.get(ss + r, 0), mx + r)
                ndt[ss - r] = max(ndt.get(ss - r, 0), mx)
                ndt[ss] = max(ndt.get(ss, 0), mx)
            dt = ndt

        return dt[0]