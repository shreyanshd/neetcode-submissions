class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def _insert(self, node: TreeNode, key: int) -> TreeNode:
        if not node:
            return TreeNode(key)
        if key == node.key:
            return node
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def _delete(self, node: TreeNode, key: int) -> TreeNode:
        if not node:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            tmp = self._minNode(node.right)
            node.key = tmp.key
            node.right = self._delete(node.right, tmp.key)
        return node


    def _minNode(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

    def _search(self, node: TreeNode, key: int) -> bool:
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def add(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def remove(self, key: int) -> None:
        self.root = self._delete(self.root, key)

    def contains(self, key: int) -> bool:
        return self._search(self.root, key)


class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.buckets = [BST() for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if not self.contains(key):
            self.buckets[idx].add(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if self.contains(key):
            self.buckets[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return self.buckets[idx].contains(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)