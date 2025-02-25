class Solution:
    def climbStairs(self, n: int) -> int:
        a1, a2 = 1, 2
        temp = n
        while n-2 > 0:
            a1 += a2
            a2 += a1
            n -= 2
        if temp % 2:
            return a1
        else:
            return a2
        