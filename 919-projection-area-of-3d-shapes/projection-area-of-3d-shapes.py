class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        front = grid[0] 
        side = max(grid[0])
        top = len(grid) * len(grid[0]) - grid[0].count(0)
        for i in range(1, len(grid)):
            side += max(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] > front[j]:
                    front[j] = grid[i][j]
                    print(front)
            if 0 in grid[i]:
                top -= grid[i].count(0)
                # print(top)
        # print(top, sum(front), side)
        return top + sum(front) + side