class ProductOfNumbers:

    def __init__(self):
        self.num_lst = []
        self.length = 0

    def add(self, num: int) -> None:
        if not len(self.num_lst) or not self.num_lst[-1]:
            self.num_lst.append(num)
            return
        self.num_lst.append(self.num_lst[-1]*num)
    
    def getProduct(self, k: int) -> int:
        # print(self.num_lst, k)
        if self.num_lst[-k]:
            if k+1 <= len(self.num_lst) and self.num_lst[-k-1]:
                return self.num_lst[-1] // self.num_lst[-k-1] if 0 not in self.num_lst[-k:] else 0
            else:
                return self.num_lst[-1] if 0 not in self.num_lst[-k:] else 0
        return 0
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)