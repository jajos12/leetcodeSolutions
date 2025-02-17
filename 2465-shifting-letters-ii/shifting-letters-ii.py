class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        my_l = [0 for i in s]
        for start, end, d in shifts:
            my_l[start] += -1 if d == 0 else 1
            if end + 1 < len(s):
                my_l[end+1] += -1 if d else 1
        for i in range(1, len(my_l)):
            my_l[i] += my_l[i-1]
        # print(my_l)
        answer = []
        for i in range(len(s)):
            char = my_l[i] + ord(s[i])
            # print(ord(s[i]), my_l[i])
            # print((char + 122)%97%26 + 97, char%97%26)
            answer.append(alpha[(my_l[i] + ord(s[i]) - 97)%26])
        return "".join(answer)
