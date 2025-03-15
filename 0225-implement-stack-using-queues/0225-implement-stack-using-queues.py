class MyStack:
    def __init__(self):
        self.deque = deque()

    def push(self, x: int) -> None:
        self.deque.append(x)
        v = len(self.deque) - 1
        i = 0
        while i < v:
            self.deque.append(self.deque.popleft())
            i += 1

    def pop(self) -> int:
        return self.deque.popleft()

    def top(self) -> int:
        return self.deque[0]

    def empty(self) -> bool:
        return len(self.deque) == 0