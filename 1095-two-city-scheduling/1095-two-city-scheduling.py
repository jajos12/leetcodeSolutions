class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: (x[0]-x[1], x[0]))
        rest, present = 0, 0
        n = len(costs)
        for i in range(n//2):
            rest += costs[n-i-1][1]
            present += costs[i][0]
        return rest + present