class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.buffer = [0] * self.size
        self.left = -1
        self.right = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.right += 1
        if self.right == self.size:
            self.right = 0
        self.buffer[self.right] = value
        self.count += 1
        if self.left == -1:
            self.left = self.right
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left += 1
        if self.left == self.size:
            self.left = 0
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.buffer[self.left]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.buffer[self.right]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()