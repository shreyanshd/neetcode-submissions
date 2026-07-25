class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        temp = []
        while self.stack and self.stack[-1][1] > self.freq[val]:
            temp.append(self.stack.pop())
        self.stack.append((val, self.freq[val]))
        while temp:
            self.stack.append(temp.pop())

    def pop(self) -> int:
        val, f = self.stack.pop()
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()