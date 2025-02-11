class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minimum = abs(min(nums))
        freq = [0]*(max(nums) + minimum + 1)
        size = len(freq)
        answer = []
        for i in nums:
            freq[minimum + i] += 1
        for i in range(size):
            for j in range(freq[i]):
                answer.append(i - minimum)
        return answer