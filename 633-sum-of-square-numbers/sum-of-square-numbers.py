class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(pow(c, 1/2))
        while left < right:
            if left**2 + right**2 == c:
                return True
            elif left**2 + right**2 > c:
                right -= 1
            else:
                left += 1
        return left**2 + right**2 == c

            
        
