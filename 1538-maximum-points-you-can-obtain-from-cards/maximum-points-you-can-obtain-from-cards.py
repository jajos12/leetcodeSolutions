class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)

        if k == n:
            return total

        window_size = n - k
        current_sum = sum(cardPoints[:window_size])
        min_sum = current_sum

        for i in range(window_size, n):
            current_sum += cardPoints[i] - cardPoints[i - window_size]
            min_sum = min(min_sum, current_sum)

        return total - min_sum
