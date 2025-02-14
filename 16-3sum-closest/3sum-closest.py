class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        nearest = float("inf")
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                sum_ = nums[left] + nums[right] + nums[i]
                if abs(target - sum_) < abs(target - nearest):
                    nearest = sum_
                if sum_ < target:
                    left += 1
                elif sum_ > target:
                    right -= 1
                else:
                    return sum_

        return nearest
