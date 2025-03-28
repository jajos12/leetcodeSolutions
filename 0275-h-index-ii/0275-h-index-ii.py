class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 1, len(citations)
        while left <= right:
            mid = (left+right)//2
            temp = [1 if mid <= i else 0 for i in citations]
            count = sum(temp)
            if mid <= count:
                left = mid+1
            else:
                right = mid-1
        return left-1