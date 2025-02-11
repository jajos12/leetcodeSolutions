class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        front = 0
        side = 0
        top = len(grid) * len(grid[0])
        for i in range(len(grid)):
            side += max(grid[i])
            max_col = 0
            for j in range(len(grid[i])):
                max_col = max(max_col, grid[j][i])
            front += max_col
            if 0 in grid[i]:
                top -= grid[i].count(0)
                # print(top)
        # print(top, front, side)
        return top + front + side