class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        while not n%2:
            n //= 2
        i = 3
        ans = 1
        while i*i <= n:
            count = 0
            while n%i == 0:
                count += 1
                n //= i
            ans *= (count+1)
            i += 2
        return ans if n == 1 else ans*2