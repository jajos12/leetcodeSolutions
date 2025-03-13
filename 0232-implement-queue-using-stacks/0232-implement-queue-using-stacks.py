class MyQueue:

    def __init__(self):
        self.stk = []
        self.top = 0
        
    def push(self, x: int) -> None:
        self.stk.append(x)

    def pop(self) -> int:
        self.top += 1
        return self.stk[self.top-1]

    def peek(self) -> int:
        return self.stk[self.top]

    def empty(self) -> bool:
        return self.top >= len(self.stk)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()