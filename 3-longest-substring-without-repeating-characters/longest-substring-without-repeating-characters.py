class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        my_set = set()
        left, right = 0, 0
        while right < len(s):
            if s[right] not in my_set:
                my_set.add(s[right])
                right += 1
                answer = max(answer, len(my_set))
            else:
                my_set.remove(s[left])
                left += 1
            # print(my_set, answer, left, right)
        return answer
        