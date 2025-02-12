class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do no
        t return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        while k:
            # print(nums)
            nums.insert(0, nums[right])
            nums.pop(right+1)
            k -= 1