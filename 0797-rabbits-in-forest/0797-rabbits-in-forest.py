class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        my_s = defaultdict(int)
        answer = 0
        for i in answers:
            if my_s[i] >= i+1:
                my_s[i] = 0
            if 0 == my_s[i] or my_s[i] > i+1 or i == 0:
                answer += i+1
            my_s[i] += 1
        return answer