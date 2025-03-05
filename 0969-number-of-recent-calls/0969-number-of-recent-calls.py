class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        i = len(self.queue)-1
        while i > -1 and t - 3000 <= self.queue[i] <= t:
            i -= 1
        return len(self.queue) - i - 1
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)