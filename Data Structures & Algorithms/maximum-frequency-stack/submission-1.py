class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.maxCount = 0
        self.stacks = {}  # count -> [val]

    def push(self, val: int) -> None:
        self.count[val] += 1
        if self.count[val] > self.maxCount:
            self.maxCount = self.count[val]
            self.stacks[self.count[val]] = []
        self.stacks[self.count[val]].append(val)

    def pop(self) -> int:
        val = self.stacks[self.maxCount].pop()
        self.count[val] -= 1
        if not self.stacks[self.maxCount]:
            del self.stacks[self.maxCount]
            self.maxCount -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()