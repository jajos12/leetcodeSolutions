class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def powe(x, n):
            if n == 0:
                return 1
            half = (powe(x, n // 2))%(10**9+7)
            if n % 2 == 0:
                return (half * half)%(10**9+7)
            else:
                return (half * half * x)%(10**9+7)
        sth = n//2 + n%2
        return (powe(4, n-sth) * powe(5, sth))%(10**9+7)
        