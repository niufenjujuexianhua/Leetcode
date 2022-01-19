class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.ls = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        # if self.hasNext():
        #     while self.ls and not self.ls[-1].isInteger():
        #         last = self.ls.pop()
        #         self.ls.extend(last.getList()[::-1])
        return self.ls.pop().getInteger()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.ls:
            if self.ls[-1].isInteger():
                return True
            last = self.ls.pop()
            self.ls.extend(last.getList()[::-1])
        return False