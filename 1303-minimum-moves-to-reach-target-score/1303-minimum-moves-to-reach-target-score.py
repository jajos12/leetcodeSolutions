class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles and target > 1:
            count += target%2 + 1
            target //= 2
            maxDoubles -= 1
        return count + (target-1 if target >= 1 else 0)