class MyHashSet:

    def __init__(self):
        self.state = [False] * 1000001

    def add(self, key: int) -> None:
        self.state[key] = True

    def remove(self, key: int) -> None:
        self.state[key] = False

    def contains(self, key: int) -> bool:
        return self.state[key] is True

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)