class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sum_, i = 0, 0
        while i < len(costs):
            if sum_ + costs[i] > coins:
                return i
            else:
                sum_ += costs[i]
                i += 1
        return i