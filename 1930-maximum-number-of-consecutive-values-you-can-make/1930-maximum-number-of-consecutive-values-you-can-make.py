class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        if coins[0] > 1:
            return 1
        x = 1
        for i in coins:
            if i > x:
                return x 
            x += i
        return x