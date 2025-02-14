class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t = Counter(t)
        left = 0
        min_length = len(s) + 1
        temp_dict = Counter()
        answer = ""
        for right in range(len(s)):
            temp_dict[s[right]] += 1
            # print(temp_dict, hash_t)
            while hash_t <= temp_dict:
                answer = s[left:right+1] if right - left < min_length else answer
                min_length = min(min_length, right-left)
                temp_dict[s[left]] -= 1
                left += 1 
            while left < right and s[left] not in hash_t:
                temp_dict[s[left]] -= 1
                left += 1
        # while right < len(s):
        #     if s[left] not in hash_t:
        #         left += 1
        #     else:
        #         if hash_t <= temp_dict and min_length > len(s[left:right+1]):
        #             min_length = len(s[left:right+1])
        #             temp_dict[s[left]] -= 1
        #             if temp_dict[s[left]] == 0:
        #                 del temp_dict[s[left]] 
        #             answer = s[left:right]
        #             left += 1
        #         temp_dict[s[right]] += 1
        #         right += 1
        #         print(temp_dict, answer, hash_t <= temp_dict, right, left)
        return answer