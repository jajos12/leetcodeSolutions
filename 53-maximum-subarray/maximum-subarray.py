class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] 
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0  # Reset if the running sum becomes negative
            curr_sum += num
            max_sum = max(max_sum, curr_sum)  
        return max_sum