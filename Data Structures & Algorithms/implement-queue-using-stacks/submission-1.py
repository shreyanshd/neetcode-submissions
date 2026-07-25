class MyQueue:

    def __init__(self):
        self.stack = []
        self.reverse_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.reverse_stack:
            while self.stack:
                self.reverse_stack.append(self.stack.pop())
        return self.reverse_stack.pop()

    def peek(self) -> int:
        if self.reverse_stack:
            return self.reverse_stack[-1]
        else:
            return self.stack[0]

    def empty(self) -> bool:
        return (len(self.stack) + len(self.reverse_stack)) == 0 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()