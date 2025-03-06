class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.key = k
        self.count = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count += 1
        else:
            self.count = 0

        return self.count >= self.key
