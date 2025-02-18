class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        diff = [0] * (len(nums) + 2)
        answer = 0
        for i in requests:
            diff[i[0]] += 1
            diff[i[1]+1] -= 1
        for i in range(1, len(diff)):
            diff[i] += diff[i-1]

        diff.sort()
        for i, j in zip(nums, diff[2:]):
            answer += i*j
        return answer%(10**9+7)