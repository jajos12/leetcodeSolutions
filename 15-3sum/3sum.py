class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate numbers
                continue

            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                sum_ = nums[left] + nums[right]
                if sum_ == target:
                    answer.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif sum_ < target:
                    left += 1
                else:
                    right -= 1

        return answer
