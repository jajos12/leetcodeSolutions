class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        my = defaultdict(int)
        ans = 0
        for i in nums:
            if i not in my:
                my[i] += 1
                if i**0.5 in my:
                    my[i] += my[i**0.5]
            ans = max(my[i], ans)
        return ans if ans > 1 else -1