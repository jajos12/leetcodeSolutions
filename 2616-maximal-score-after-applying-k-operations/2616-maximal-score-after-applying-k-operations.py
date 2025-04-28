class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        score = 0
        for _ in range(k):
            temp = heapq.heappop(nums)
            score += temp 
            heapq.heappush(nums, -(abs(temp)/3).__ceil__())
        return -score