class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int)
        d[0], run_sum = 1, 0
        count = 0
        for i in range(len(nums)):
            run_sum += nums[i]
            count += d[run_sum-goal]
            d[run_sum] += 1
        return count