class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if len(flowerbed) == 1:
            return True if (flowerbed[0] == 0 and n <= 1) or (flowerbed[0] == 1 and n==0) else False
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            count += 1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                count += 1
                flowerbed[i] = 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            count += 1
        return count >= n