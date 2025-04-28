class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapq.heapify(piles)
        for _ in range(k):
            to_be_halfed = heapq.heappop(piles)
            heapq.heappush(piles, -(abs(to_be_halfed)//2 + to_be_halfed%2))
        return -sum(piles)