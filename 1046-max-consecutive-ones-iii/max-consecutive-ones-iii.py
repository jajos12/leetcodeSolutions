class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length, hash_one, left = 0, defaultdict(int), 0
        for right in range(len(nums)):
            hash_one[nums[right]] += 1
            # print(hash_one, max_length)
            while hash_one[0] > k:
                hash_one[nums[left]] -= 1
                left += 1
            max_length = max(max_length, right-left+1)
        return max_length