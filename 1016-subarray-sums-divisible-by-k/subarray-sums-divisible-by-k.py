class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        run_sum = 0
        count = 0
        for i in range(len(nums)):
            run_sum += nums[i]
            # print(d)
            count += d[run_sum%k]
            d[run_sum%k] += 1
        return count