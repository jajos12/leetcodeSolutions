class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        curr_sum, count = 0, 0
        for i in nums:
            curr_sum += i
            if curr_sum - k in d:
                count += d[curr_sum-k]
            if curr_sum in d:
                d[curr_sum] += 1
            else:
                d[curr_sum] = 1
        return count