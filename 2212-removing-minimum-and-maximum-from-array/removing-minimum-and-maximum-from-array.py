class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        min_val, max_val = float("inf"), float("-inf")
        length = len(nums)
        indices = [0, length-1]
        for n in range(len(nums)):
            # print(min_val, max_val, indices, nums[n], min_val > nums[n], max_val < nums[n])
            if min_val > nums[n]:
                min_val = nums[n]
                indices = [n, indices[1]]
            if max_val < nums[n]:
                max_val = nums[n]
                indices = [indices[0], n]
        maxim, minim = max(indices), min(indices)
        return min(length-maxim+minim+1, maxim+1, length-minim)