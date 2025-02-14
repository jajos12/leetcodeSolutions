class Solution:
    def minimumSteps(self, s: str) -> int:
        count_of_1 = 0
        answer = 0
        for i in s:
            if i == "1":
                count_of_1 += 1
            else:
                answer += count_of_1
        return answer