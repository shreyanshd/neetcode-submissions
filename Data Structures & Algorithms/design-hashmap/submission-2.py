class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, key, value):
        if not node:
            return TreeNode(key, value)
        if key == node.key:
            node.value = value
            return node
        elif key < node.key:
            node.left = self.insert(node.left, key, value)
        else:
            node.right = self.insert(node.right, key, value)
        return node

    def delete(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            tmp = self.minNode(node.right)
            node.key = tmp.key
            node.value = tmp.value
            node.right = self.delete(node.right, tmp.key)
        return node

    def minNode(self, node):
        while node.left:
            node = node.left
        return node

    def find(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self.find(node.left, key)
        else:
            return self.find(node.right, key)

    def get(self, key):
        return self.find(self.root, key)

    def add(self, key, value):
        self.root = self.insert(self.root, key, value)

    def remove(self, key):
        self.root = self.delete(self.root, key)

class MyHashMap:

    def __init__(self):
        self.size = 10007
        self.buckets = [BST() for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        self.buckets[idx].add(key, value)

    def get(self, key: int) -> int:
        idx = self.hash(key)
        value = self.buckets[idx].get(key)
        return value if value is not None else -1

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        self.buckets[idx].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)