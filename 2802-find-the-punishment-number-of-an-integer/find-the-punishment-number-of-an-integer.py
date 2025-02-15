class Solution:
    def punishmentNumber(self, n: int) -> int:
        punishment  =  [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
        left = 0
        answer = 0
        while left < len(punishment) and punishment[left] <= n:
            if punishment[left] <= n:
                answer += punishment[left] ** 2
            left += 1
        return answer