class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(left, right):
            if left > right:
                return -1
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                return helper(mid+1, right)
            else:
                return helper(left, mid-1)
        res = helper(0, len(nums)-1)
        return res