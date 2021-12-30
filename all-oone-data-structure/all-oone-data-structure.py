class Node(object):

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.keys = set()

class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0, self.head)
        self.head.next = self.tail
        self.mapping = defaultdict(lambda: self.head)

    def inc(self, key: str) -> None:
        cur = self.mapping[key]
        cur.keys.discard(key)
            
        if cur.val + 1 == cur.next.val:
            new = cur.next
        else:
            new = Node(cur.val + 1, cur, cur.next)
            new.prev.next = new.next.prev = new
            
        new.keys.add(key)
        self.mapping[key] = new

        if not cur.keys and cur.val != 0:
            cur.prev.next, cur.next.prev = cur.next, cur.prev
            
    def dec(self, key: str) -> None:
        if not key in self.mapping: return

        cur = self.mapping[key]
        cur.keys.discard(key)
        self.mapping.pop(key)

        if cur.val > 1:
            if cur.val - 1 == cur.prev.val:
                new = cur.prev
            else:
                new = Node(cur.val - 1, cur, cur.next)
                new.prev.next = new.next.prev = new
                
            new.keys.add(key)
            self.mapping[key] = new

        if not cur.keys:
            cur.prev.next, cur.next.prev = cur.next, cur.prev

    def getMaxKey(self) -> str:
        if not self.tail.prev.val: return ''
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if not self.head.next.val: return ''
        return next(iter(self.head.next.keys))