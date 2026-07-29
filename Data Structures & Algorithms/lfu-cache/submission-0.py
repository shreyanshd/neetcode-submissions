class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def pushRight(self, node: ListNode):
        left = self.tail.prev
        left.next = node
        node.prev = left
        node.next = self.tail
        self.tail.prev = node
        self.size += 1
    
    def pop(self, node: ListNode):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left
        node.next = None
        node.prev = None
        self.size -= 1

    def popLeft(self) -> ListNode:
        if self.length() == 0:
            return None
        node = self.head.next
        self.pop(node)
        return node

    def length(self):
        return self.size


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeMap = {}
        self.listMap = collections.defaultdict(LinkedList)
        self.minFreq = 0

    def updateCount(self, node: ListNode):
        count = node.freq
        self.listMap[count].pop(node)
        
        if self.minFreq == count and self.listMap[count].length() == 0:
            self.minFreq += 1
        
        node.freq += 1
        self.listMap[node.freq].pushRight(node)

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.updateCount(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self.updateCount(node)
            return
        
        if len(self.nodeMap) == self.capacity:
            node = self.listMap[self.minFreq].popLeft()
            self.nodeMap.pop(node.key)
        
        node = ListNode(key, value)
        self.nodeMap[key] = node
        self.listMap[1].pushRight(node)
        self.minFreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)