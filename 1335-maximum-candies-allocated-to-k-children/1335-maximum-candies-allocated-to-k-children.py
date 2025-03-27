class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        while l <= r:
            mid = (l+r)//2
            if sum(i//mid for i in candies) >= k:
                l = mid+1
            else:
                r = mid-1
        return r