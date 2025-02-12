class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict = Counter(s)
        temp = set()
        subs_rep = 0
        answer = []
        length = 0
        # print(my_dict)
        for i in s:
            my_dict[i] -= 1
            if i not in temp:
                temp.add(i)
                subs_rep += my_dict[i]
            else:
                subs_rep -= 1
            length += 1
            if subs_rep == 0:
                answer.append(length)
                length = 0
            # print(i, answer, subs_rep)
        return answer