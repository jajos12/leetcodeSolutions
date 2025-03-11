class Solution:
    def trailingZeroes(self, n: int) -> int:
        five, even = n-n%5, n-n%2
        amount = 0
        def power(n):
            five = 5
            answer = 0
            while n%five == 0:
                answer += 1
                five *= 5
            return answer

        while five > 0:
            amount += power(five)
            five -= 5
            even -= 2
        return amount