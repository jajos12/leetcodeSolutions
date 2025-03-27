class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1
        while left < right and nums[left] > nums[right]:
            mid = (left+right)//2
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid+1
        return nums[left]