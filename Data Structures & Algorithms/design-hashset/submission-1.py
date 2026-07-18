class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.k = 10**4
        self.buckets = [ListNode(0) for _ in range(self.k)]

    def add(self, key: int) -> None:
        curr = self.bucket(key)
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.bucket(key)
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.bucket(key)
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False
    
    def bucket(self, key: int) -> ListNode:
        return self.buckets[key % self.k]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)